from flask import Flask, jsonify

from flask_cors import CORS

from helper import containerMaker
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)


@app.route('/')
def index():
    return jsonify({
        "message": "テスト!!"
    })


@app.route('/servers', methods=['GET'])
def makeServer():
    deployment = containerMaker.create_deployment_object()
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
