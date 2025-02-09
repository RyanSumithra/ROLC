from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
optimize_collection = db["optimization"]

optimize_bp = Blueprint("optimize", __name__)


def optimize_routes(vehicles, delivery_locations):
    optimized_routes = {}
    for vehicle in vehicles:
        vehicle_route = random.sample(delivery_locations, len(delivery_locations) // len(vehicles))
        optimized_routes[vehicle["vehicle_id"]] = vehicle_route
    return optimized_routes


@optimize_bp.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    vehicles = data.get("vehicles", [])
    delivery_locations = data.get("delivery_locations", [])

    if not vehicles or not delivery_locations:
        return jsonify({"error": "Missing required fields (vehicles or delivery_locations)"}), 400

    optimized_routes = optimize_routes(vehicles, delivery_locations)

    # Save optimization results to the database
    optimize_collection.insert_one({"optimized_routes": optimized_routes})

    return jsonify({"optimized_routes": optimized_routes}), 200
