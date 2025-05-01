from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/daily')
def daily():
    return jsonify({"message": "Daily summary here"})

@app.route('/activities')
def activities():
    return jsonify({"activities": []})

@app.route('/healthz')
def healthz():
    return 'OK', 200


def handler(request, context):
    return app(request.environ, start_response)
