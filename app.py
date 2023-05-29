import uuid
from flask import Flask, request
from flask_smorest import abort
# from db import stores, items
from flask_smorest import Api
from resources.store import store_blp
from resources.item import item_blp
from db import db
from models.item import ItemModel
from models.store import StoreModel

def create_app():


    app = Flask(__name__)
    app.config["API_TITLE"] = "Store API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()


    api.register_blueprint(store_blp)
    api.register_blueprint(item_blp)



    return app









if __name__ == "__main__":
    create_app.run(debug=True)