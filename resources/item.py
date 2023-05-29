from models.store import StoreModel
from models.item import ItemModel
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import uuid
from schema import ItemSchema
from db import db

item_blp = Blueprint("items", "items", description="Items operations")

@item_blp.route("/items")
class Items(MethodView):
    @item_blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
@item_blp.route("/item")
class Item(MethodView):
    @item_blp.arguments(ItemSchema)
    @item_blp.response(200, ItemSchema)
    def get(self, item_data):
        try:
            if ItemModel.query.get(item_data["id"]):
                return ItemModel.query.get(item_data["id"])
            else:
                abort(404, message="Item not found!")
        except KeyError:
            abort(404, message="Invalid input")

    @item_blp.arguments(ItemSchema)
    @item_blp.response(200, ItemSchema)
    def post(self, item_data):
        try:
            if StoreModel.query.get(item_data["store_id"]):

                item = ItemModel(name=item_data["name"], price=item_data["price"], store_id=item_data["store_id"])
                db.session.add(item)
                db.session.commit()

                items = ItemModel.query.all()
                for item in items:
                    print(item.id, item.name, item.price, item.store_id)
                return item
            else:
                abort(404, message="Store not found!")
        except:
            abort(404, message="Invalid input received!")

    @item_blp.arguments(ItemSchema)
    def put(self, item_data):
        try:
            item_id = item_data["id"]
            item = ItemModel.query.get(item_id)
            if item:
                item.name = item_data["name"]
                item.price = item_data["price"]
                item.store_id = item_data["store_id"]

                db.session.add(item)
                db.session.commit()

                return {"message": "Item updated!"}

            else:
                abort(404, message="Item not found!")
        except:
            abort(404, message="Invalid data received!")

    @item_blp.arguments(ItemSchema)
    @item_blp.response(200, ItemSchema)
    def delete(self, item_data):
        try:
            item_id = item_data["id"]
            item = ItemModel.query.get(item_id)
            if item:
                db.session.delete(item)
                db.session.commit()
                return {"message": "Item deleted!"}
            else:
                print("here")
                abort(404, message="Item not found!")
        except KeyError:
            abort(404, message="Invalid data received!")