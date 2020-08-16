from flask import Flask, jsonify
from kubernetes import client, config

from flask_cors import CORS

from helper import containerMaker
import time

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
    deployment = containerMaker.create_deployment_object()
    podname = containerMaker.create_deployment(
        apps_v1, core_v1_api, deployment)
    containerMaker.create_LoadBalancer(core_v1_api)

    while(True):
        time.sleep(3)
        app.logger.debug("Made pod is ", podname)
        if(containerMaker.read_pod_status(core_v1_api, podname) == "Running"):
            break

    return jsonify({
        "msg": "サーバメイキングテスト!!"
    })


@app.route('/servers', methods=['DELETE'])
def deleteServer():

    containerMaker.delete_deployment(apps_v1)
    containerMaker.delete_LoadBalancer(core_v1_api)

    return jsonify({
        "msg": "サーバデリートテスト!!"
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
