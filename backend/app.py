from flask import Flask, jsonify, request

from helper import containerMaker
from helper import ttydChecker

import time
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

listOfArticles = [
    {
        "id": 0,
        "Title": '外に接続できない！',
        "deployImage": "nginx:1.12",
        "detail": "サーバーの外にアクセスできません。8.8.8.8にpingが通るようにしてください。",
    },
    {
        "id": 1,
        "Title": 'sshできない！',
        "deployImage": "tsl0922/ttyd",
        "detail": "サーバーにsshで接続できません。ssh test@localhostができるようにしてください。",
    }
]

deploymentsMap = {}


@app.route('/api')
def index():
    return jsonify({
        "message": "テスト!!"
    })


@app.route('/api/articles', methods=['GET'])
def returnArticleList():
    resList = []
    for article in listOfArticles:
        formated = {
            "id": article["id"],
            "Title": article["Title"]
        }
        resList.append(formated)
    return jsonify(resList)


@app.route('/api/articles/<int:idNum>', methods=['GET'])
def returnArticle(idNum=None):
    return jsonify(listOfArticles[idNum])


@app.route('/api/articles/new', methods=['POST'])
def makeNewArticle():
    data = request.get_json()

    app.logger.debug("Posted Article ", data)

    data["id"] = len(listOfArticles)
    data["report"] = "HogeHoge"

    listOfArticles.append(data)

    return jsonify({
        "msg": "Make new article!!!"
    })


@app.route('/api/servers/<int:idNum>', methods=['GET'])
def makeServer(idNum=None):
    deployArticle = listOfArticles[idNum]
    deployment = containerMaker.create_deployment_object(
        deployArticle["deployImage"])
    podname = containerMaker.create_deployment(deployment)
    containerMaker.create_LoadBalancer(deployment.metadata.name)

    while(True):
        time.sleep(3)
        app.logger.debug("Made pod is ", podname)
        app.logger.debug(ttydChecker.comfirmTtydStart(
            deployment.metadata.name))
        if ttydChecker.comfirmTtydStart(deployment.metadata.name) == 200:
            break

    # redisにする
    deploymentsMap[idNum] = deployment.metadata.name

    return jsonify({
        "msg": "サーバメイキングテスト!!",
        "Made pod name": podname
    })


@app.route('/api/servers/<int:idNum>', methods=['DELETE'])
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
