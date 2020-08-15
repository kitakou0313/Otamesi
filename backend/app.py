from flask import Flask, jsonify
from kubernetes import client, config

from flask_cors import CORS

from helper import containerMaker

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

config.load_incluster_config()

apps_v1 = client.AppsV1Api()  # for server deployment
core_v1_api = client.CoreV1Api()  # for LB deployment


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

    containerMaker.create_LoadBalancer(core_v1_api)

    return jsonify({
        "msg": "サーバメイキングテスト!!"
    })


@app.route('/servers', methods=['DELETE'])
def deleteServer():

    containerMaker.delete_deployment(apps_v1)
    containerMaker.delete_LoadBalancer(core_v1_api)

    return jsonify({
        "msg": "サーバデリーとテスト!!"
    })


if __name__ == '__main__':
    app.run()
