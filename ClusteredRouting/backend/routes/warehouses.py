from flask import Blueprint, request, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
warehouses_collection = db["warehouses"]

warehouses_bp = Blueprint("warehouses", __name__)

@warehouses_bp.route("/warehouses", methods=["GET"])
def get_warehouses():
    warehouses = list(warehouses_collection.find({}, {"_id": 0}))
    return jsonify(warehouses)

@warehouses_bp.route("/warehouse", methods=["POST"])
def add_warehouse():
    data = request.json
    if not all(key in data for key in ("warehouse_id", "location", "inventory")):
        return jsonify({"error": "Missing required warehouse fields"}), 400
    warehouses_collection.insert_one(data)
    return jsonify({"message": "Warehouse added successfully"}), 201

@warehouses_bp.route("/warehouse/<warehouse_id>", methods=["PUT"])
def update_warehouse(warehouse_id):
    data = request.json
    if not any(key in data for key in ("location", "inventory")):
        return jsonify({"error": "Missing fields to update"}), 400
    warehouses_collection.update_one(
        {"warehouse_id": warehouse_id},
        {"$set": data}
    )
    return jsonify({"message": "Warehouse updated successfully"})

@warehouses_bp.route("/warehouse/<warehouse_id>", methods=["DELETE"])
def delete_warehouse(warehouse_id):
    warehouses_collection.delete_one({"warehouse_id": warehouse_id})
    return jsonify({"message": "Warehouse deleted successfully"})
