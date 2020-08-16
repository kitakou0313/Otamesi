from flask import Flask, jsonify

from flask_cors import CORS

from helper import containerMaker
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

listOfArticles = [
    {
        "id": 0,
        "Title": 'Test',
        "deployImage": "tsl0922/ttyd",
        "report": "Test you desu",
    },
    {
        "id": 1,
        "Title": 'Test2',
        "deployImage": "tsl0922/ttyd",
        "report": "Test2 you desu",
    }
]


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


@app.route('/servers/<int:idNum>', methods=['GET'])
def makeServer(idNum=None):
    deployArticle = listOfArticles[idNum]
    deployment = containerMaker.create_deployment_object(
        deployArticle["deployImage"])
    podname = containerMaker.create_deployment(deployment)
    containerMaker.create_LoadBalancer()

    while(True):
        time.sleep(3)
        app.logger.debug("Made pod is ", podname)
        if(containerMaker.read_pod_status(podname) == "Running"):
            break

    return jsonify({
        "msg": "サーバメイキングテスト!!",
        "Made pod name": podname
    })


@app.route('/servers', methods=['DELETE'])
def deleteServer():

    containerMaker.delete_deployment()
    containerMaker.delete_LoadBalancer()

    return jsonify({
        "msg": "サーバデリートテスト!!"
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
