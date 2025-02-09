from flask import Flask, send_from_directory
from flask_cors import CORS
from models.vehicle import vehicle_bp
from models.warehouse import warehouse_bp
from models.item import item_bp
from models.order import orders_bp
from config import Config
import os


# Create the Flask app
def create_app():
    app = Flask(__name__, static_folder='frontend/build/static', template_folder='frontend/build')

    # Enable CORS (Cross-Origin Resource Sharing) for front-end and back-end communication
    CORS(app)

    # Load the configuration settings
    app.config.from_object(Config)

    # Register Blueprints for routes
    app.register_blueprint(vehicle_bp, url_prefix="/api/vehicles")
    app.register_blueprint(warehouse_bp, url_prefix="/api/warehouses")
    app.register_blueprint(item_bp, url_prefix="/api/items")
    app.register_blueprint(orders_bp, url_prefix="/api/orders")

    # Serve React Frontend
    @app.route("/", methods=["GET"])
    def serve_frontend():
        return send_from_directory(app.template_folder, "index.html")

    # Catch-all for React routing (Handle client-side routing in production)
    @app.route("/<path:path>", methods=["GET"])
    def serve_static(path):
        return send_from_directory(app.static_folder, path)

    return app


# Run the Flask app
if __name__ == "__main__":
    app = create_app()

    # Run in debug mode for development (Make sure to use production mode in production)
    app.run(debug=True, host="0.0.0.0", port=5000)
