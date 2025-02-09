from flask import Flask
from models.vehicle import vehicle_bp
from models.warehouse import warehouse_bp
from models.item import item_bp
from models.order import orders_bp
from config import Config


def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(vehicle_bp, url_prefix="/api")
    app.register_blueprint(warehouse_bp, url_prefix="/api")
    app.register_blueprint(item_bp, url_prefix="/api")
    app.register_blueprint(orders_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()

    # Run the Flask app
    app.run(debug=True)
