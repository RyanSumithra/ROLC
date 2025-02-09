from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
vehicles_collection = db["vehicles"]

vehicle_bp = Blueprint("vehicle", __name__)

# Fetch all vehicles
@vehicle_bp.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = list(vehicles_collection.find({}, {"_id": 0}))
    return jsonify(vehicles), 200

# Add a new vehicle
@vehicle_bp.route("/vehicle", methods=["POST"])
def add_vehicle():
    data = request.json

    # Validate required fields
    required_fields = ["vehicle_id", "capacity", "speed", "current_location"]
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required vehicle fields"}), 400

    # Insert the vehicle into the database
    vehicles_collection.insert_one(data)
    return jsonify({"message": "Vehicle added successfully"}), 201

# Update a vehicle
@vehicle_bp.route("/vehicle/<vehicle_id>", methods=["PUT"])
def update_vehicle(vehicle_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Update the vehicle in the database
    result = vehicles_collection.update_one(
        {"vehicle_id": vehicle_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Vehicle not found"}), 404

    return jsonify({"message": "Vehicle updated successfully"}), 200

# Delete a vehicle
@vehicle_bp.route("/vehicle/<vehicle_id>", methods=["DELETE"])
def delete_vehicle(vehicle_id):
    result = vehicles_collection.delete_one({"vehicle_id": vehicle_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Vehicle not found"}), 404

    return jsonify({"message": "Vehicle deleted successfully"}), 200
