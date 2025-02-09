import os


class Config:
    """Base configuration class."""
    # Flask settings
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key_here")  # Change this for production
    DEBUG = os.environ.get("FLASK_DEBUG", "True") == "True"  # Whether to run in debug mode

    # MongoDB settings
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/logistics")

    # You can add more configuration variables here as needed
    # For example, logging, email settings, etc.


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    # Add more development-specific settings if necessary


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    # Production-specific settings (like a more secure secret key)
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_production_secret_key_here")


class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/test_logistics"  # Separate test database
