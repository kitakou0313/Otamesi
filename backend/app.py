from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import redis

from helper import containerMaker
from helper import ttydChecker

import time
import requests

r = redis.Redis(host='redis', port=6379, db=0)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///article.sqlite'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    deployImage = db.Column(db.Text(), nullable=False)
    detail = db.Column(db.Text(), nullable=False)

    def __init__(self, title, deployImage, detail):
        self.title, self.deployImage, self.detail = title, deployImage, detail


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", 'title', 'deployImage', 'detail')


articleSchema = ArticleSchema()
articlesSchema = ArticleSchema(many=True)


listOfArticles = [
    {
        "title": '外に接続できない！',
        "deployImage": "nginx:1.12",
        "detail": "サーバーの外にアクセスできません。8.8.8.8にpingが通るようにしてください。",
    },
    {
        "title": 'sshできない！',
        "deployImage": "tsl0922/ttyd",
        "detail": "サーバーにsshで接続できません。ssh test@localhostができるようにしてください。",
    }
]

db.create_all()
for article in listOfArticles:
    entryArticle = Article(
        article["title"], article["deployImage"], article["detail"])
    db.session.add(entryArticle)
    db.session.commit()


@app.route('/api')
def index():
    return jsonify({
        "message": "テスト!!"
    })


@app.route('/api/articles', methods=['GET'])
def returnArticleList():
    articles = Article.query.all()
    return articlesSchema.jsonify(articles)


@app.route('/api/articles/<int:idNum>', methods=['GET'])
def returnArticle(idNum=None):
    article = Article.query.get(idNum)
    return articleSchema.jsonify(article)


@app.route('/api/articles/new', methods=['POST'])
def makeNewArticle():

    newArticle = Article(
        request.json["title"], request.json["deployImage"], request.json["detail"])

    db.session.add(newArticle)
    db.session.commit()
    return jsonify({
        "msg": "Make new article!!!"
    })


@app.route('/api/servers/<int:idNum>', methods=['GET'])
def makeServer(idNum=None):
    deployArticle = Article.query.get(idNum)

    deployment = containerMaker.create_deployment_object(
        deployArticle.deployImage)

    podname = containerMaker.create_deployment(deployment)
    containerMaker.create_LoadBalancer(deployment.metadata.name)

    while(True):
        time.sleep(2)
        app.logger.debug("Made pod is ", podname)
        app.logger.debug(ttydChecker.comfirmTtydStart(
            deployment.metadata.name))
        if ttydChecker.comfirmTtydStart(deployment.metadata.name) == 200:
            break

    # redisにする
    r.set(idNum, deployment.metadata.name)

    return jsonify({
        "msg": "サーバメイキングテスト!!",
        "Made pod name": podname
    })


@app.route('/api/servers/<int:idNum>', methods=['DELETE'])
def deleteServer(idNum=None):

    deletingDeployName = r.get(idNum).decode()
    app.logger.debug("Delete img name is ", deletingDeployName)

    containerMaker.delete_deployment(deletingDeployName)
    containerMaker.delete_LoadBalancer(deletingDeployName)

    r.delete(idNum)

    return jsonify({
        "msg": "サーバデリートテスト!!"
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
