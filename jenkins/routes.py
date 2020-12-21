from flask import jsonify, request
from jenkins import app
from jenkins import varenv
from jenkins.tasks import build_image_docker


@app.route('/')
def hello_world():
    return varenv.WORKDIR_APP


@app.route('/build_image', methods=['POST'])
def build_image():
    data = request.get_json()
    build_image_docker.delay(data["tag"])
    return jsonify({"response": "Task sent to the worker!"})
