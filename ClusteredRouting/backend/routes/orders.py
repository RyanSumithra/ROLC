from flask import Blueprint, request, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
orders_collection = db["orders"]

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders", methods=["GET"])
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    return jsonify(orders)

@orders_bp.route("/order", methods=["POST"])
def place_order():
    data = request.json
    if not all(key in data for key in ("customer_name", "item_id", "delivery_lat", "delivery_lon", "quantity")):
        return jsonify({"error": "Missing required order fields"}), 400
    orders_collection.insert_one(data)
    return jsonify({"message": "Order placed successfully"}), 201
