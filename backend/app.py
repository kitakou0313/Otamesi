from flask import Flask, jsonify
from kubernetes import client, config

from helper import containerMaker

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

config.load_incluster_config()
apps_v1 = client.AppsV1Api()


@app.route('/')
def index():
    return jsonify({
        "message": "テスト!!"
    })


@app.route('/servers', methods=['GET'])
def makeServer():

    apps_v1 = client.AppsV1Api()

    deployment = containerMaker.create_deployment_object()
    containerMaker.create_deployment(apps_v1, deployment)

    return jsonify({
        "msg": "サーバメイキングテスト!!"
    })


@app.route('/servers', methods=['DELETE'])
def deleteServer():

    containerMaker.delete_deployment(apps_v1)

    return jsonify({
        "msg": "サーバデリーとテスト!!"
    })


if __name__ == '__main__':
    app.run()
