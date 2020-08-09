from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return jsonify({
        "message": "テスト!!"
    })


if __name__ == '__main__':
    app.run()
