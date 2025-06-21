from flask import Blueprint, jsonify

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return jsonify({"message": "Pizza API running!"})
