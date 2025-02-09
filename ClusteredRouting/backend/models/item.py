from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["logistics"]
items_collection = db["items"]

item_bp = Blueprint("item", __name__)

# Fetch all items
@item_bp.route("/items", methods=["GET"])
def get_items():
    items = list(items_collection.find({}, {"_id": 0}))
    return jsonify(items), 200

# Add a new item
@item_bp.route("/item", methods=["POST"])
def add_item():
    data = request.json

    # Validate required fields
    required_fields = ["item_id", "name", "category", "quantity", "price"]
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required item fields"}), 400

    # Insert the item into the database
    items_collection.insert_one(data)
    return jsonify({"message": "Item added successfully"}), 201

# Update an item
@item_bp.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Update the item in the database
    result = items_collection.update_one(
        {"item_id": item_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": "Item updated successfully"}), 200

# Delete an item
@item_bp.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    result = items_collection.delete_one({"item_id": item_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": "Item deleted successfully"}), 200
