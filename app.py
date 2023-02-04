import os

from flask import Flask
from flask_smorest import Api 
#from flask_jwt_extended import JWTManager
#from flask_migrate import Migrate

from db import db
#from blocklist import BLOCKLIST
import models 

#it's already a package in __init__.py

from resources.product import blp as ProductBlueprint
from resources.store import blp as StoreBlueprint

#from resources.tag import blp as TagBlueprint
#from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_WARN_20"] = 1
    db.init_app(app)
    # migrate = Migrate(app, db)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ProductBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app

