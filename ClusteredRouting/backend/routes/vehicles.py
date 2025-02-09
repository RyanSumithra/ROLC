from flask import Blueprint, request, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
vehicles_collection = db["vehicles"]

vehicles_bp = Blueprint("vehicles", __name__)

@vehicles_bp.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = list(vehicles_collection.find({}, {"_id": 0}))
    return jsonify(vehicles)

@vehicles_bp.route("/vehicle", methods=["POST"])
def add_vehicle():
    data = request.json
    if not all(key in data for key in ("vehicle_id", "capacity", "speed", "current_location")):
        return jsonify({"error": "Missing required vehicle fields"}), 400
    vehicles_collection.insert_one(data)
    return jsonify({"message": "Vehicle added successfully"}), 201

@vehicles_bp.route("/vehicle/<vehicle_id>", methods=["PUT"])
def update_vehicle(vehicle_id):
    data = request.json
    if not any(key in data for key in ("capacity", "speed", "current_location")):
        return jsonify({"error": "Missing fields to update"}), 400
    vehicles_collection.update_one(
        {"vehicle_id": vehicle_id},
        {"$set": data}
    )
    return jsonify({"message": "Vehicle updated successfully"})

@vehicles_bp.route("/vehicle/<vehicle_id>", methods=["DELETE"])
def delete_vehicle(vehicle_id):
    vehicles_collection.delete_one({"vehicle_id": vehicle_id})
    return jsonify({"message": "Vehicle deleted successfully"})
