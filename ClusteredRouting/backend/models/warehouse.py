from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
warehouses_collection = db["warehouses"]

warehouse_bp = Blueprint("warehouse", __name__)

# Fetch all warehouses
@warehouse_bp.route("/warehouses", methods=["GET"])
def get_warehouses():
    warehouses = list(warehouses_collection.find({}, {"_id": 0}))
    return jsonify(warehouses), 200

# Add a new warehouse
@warehouse_bp.route("/warehouse", methods=["POST"])
def add_warehouse():
    data = request.json

    # Validate required fields
    required_fields = ["warehouse_id", "location", "inventory"]
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required warehouse fields"}), 400

    # Insert the warehouse into the database
    warehouses_collection.insert_one(data)
    return jsonify({"message": "Warehouse added successfully"}), 201

# Update a warehouse
@warehouse_bp.route("/warehouse/<warehouse_id>", methods=["PUT"])
def update_warehouse(warehouse_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Update the warehouse in the database
    result = warehouses_collection.update_one(
        {"warehouse_id": warehouse_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Warehouse not found"}), 404

    return jsonify({"message": "Warehouse updated successfully"}), 200

# Delete a warehouse
@warehouse_bp.route("/warehouse/<warehouse_id>", methods=["DELETE"])
def delete_warehouse(warehouse_id):
    result = warehouses_collection.delete_one({"warehouse_id": warehouse_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Warehouse not found"}), 404

    return jsonify({"message": "Warehouse deleted successfully"}), 200
