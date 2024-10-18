from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config
import logging

# Initialize MongoDB
mongo = PyMongo()

def create_app():
    # Initialize the Flask app within the factory function
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(level=logging.DEBUG)
    # Initialize MongoDB with the app
    mongo.init_app(app)

    # Import and register routes
    from app.routes import user_blueprint
    app.register_blueprint(user_blueprint)

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error('Internal error: %s', error)
        return "500 error", 500

    return app
