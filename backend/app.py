from flask import Flask, jsonify, request

from flask_cors import CORS

from helper import containerMaker
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

listOfArticles = [
    {
        "id": 0,
        "Title": '外に接続できない！',
        "deployImage": "tsl0922/ttyd",
        "report": "Test you desu",
    },
    {
        "id": 1,
        "Title": 'FTPできない！',
        "deployImage": "tsl0922/ttyd",
        "report": "Test2 you desu",
    }
]

deploymentsMap = {}


@app.route('/')
def index():
    return jsonify({
        "message": "テスト!!"
    })


@app.route('/articles', methods=['GET'])
def returnArticleList():
    resList = []
    for article in listOfArticles:
        formated = {
            "id": article["id"],
            "Title": article["Title"]
        }
        resList.append(formated)
    return jsonify(resList)


@app.route('/articles/<int:idNum>', methods=['GET'])
def returnArticle(idNum=None):
    return jsonify(listOfArticles[idNum])


@app.route('/articles/new', methods=['POST'])
def makeNewArticle():
    data = request.get_json()

    app.logger.debug("Posted Article ", data)

    data["id"] = len(listOfArticles)
    data["report"] = "HogeHoge"

    listOfArticles.append(data)

    return jsonify({
        "msg": "Make new article!!!"
    })


@app.route('/servers/<int:idNum>', methods=['GET'])
def makeServer(idNum=None):
    deployArticle = listOfArticles[idNum]
    deployment = containerMaker.create_deployment_object(
        deployArticle["deployImage"])
    podname = containerMaker.create_deployment(deployment)
    containerMaker.create_LoadBalancer(deployment.metadata.name)

    while(True):
        time.sleep(3)
        app.logger.debug("Made pod is ", podname)
        if(containerMaker.read_pod_status(podname) == "Running"):
            break

    # redisにする
    deploymentsMap[idNum] = deployment.metadata.name

    return jsonify({
        "msg": "サーバメイキングテスト!!",
        "Made pod name": podname
    })


@app.route('/servers/<int:idNum>', methods=['DELETE'])
def deleteServer(idNum=None):

    containerMaker.delete_deployment(deploymentsMap[idNum])
    containerMaker.delete_LoadBalancer(deploymentsMap[idNum])

    del deploymentsMap[idNum]

    return jsonify({
        "msg": "サーバデリートテスト!!"
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
