from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
  
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    from app.routes import user_blueprint
    app.register_blueprint(user_blueprint)

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error('Internal error: %s', error)
        return "500 error", 500

    return app
