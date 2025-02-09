from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
orders_collection = db["orders"]

orders_bp = Blueprint("orders", __name__)

# Fetch all orders
@orders_bp.route("/orders", methods=["GET"])
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    return jsonify(orders), 200

# Place a new order
@orders_bp.route("/order", methods=["POST"])
def place_order():
    data = request.json

    # Validate required fields
    required_fields = ["customer_name", "item_id", "delivery_lat", "delivery_lon", "quantity"]
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required order fields"}), 400

    # Add order timestamp
    data["order_timestamp"] = datetime.utcnow()

    # Insert the order into the database
    orders_collection.insert_one(data)

    return jsonify({"message": "Order placed successfully"}), 201

# Update an existing order
@orders_bp.route("/order/<order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.json

    # Ensure the order ID is in the request
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Update order in the database
    result = orders_collection.update_one(
        {"order_id": order_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({"message": "Order updated successfully"}), 200

# Delete an order
@orders_bp.route("/order/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    # Delete the order from the database
    result = orders_collection.delete_one({"order_id": order_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({"message": "Order deleted successfully"}), 200
