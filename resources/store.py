from models.store import StoreModel
import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema import StoreSchema
from db import db

store_blp = Blueprint("stores", "stores", description="store operations" )

@store_blp.route("/stores")
class Stores(MethodView):
   
    @store_blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
@store_blp.route("/store")
class Store(MethodView):



    @store_blp.response(200, StoreSchema)
    def get(self):
        store_data = request.get_json()
        try:
            store = StoreModel.query.get(store_data["id"])
            return store
        except:
            abort(404, message="Invalid data received!")

    @store_blp.arguments(StoreSchema)
    @store_blp.response(200, StoreSchema)
    def post(self, store_data):

    
        try:
            store = StoreModel(name = store_data["name"])
            db.session.add(store)
            db.session.commit()

            return store
        except:
            abort(404, message="Invalid data received!")
    
    @store_blp.arguments(StoreSchema)
    def delete(self, store_data):
        try:
            store = StoreModel.query.get(store_data["id"])
            if store:
                db.session.delete(store)
                db.session.commit()
                print(store_data["id"])
                return {"message": "Store deleted"}, 200
            else:
                abort(404, message="Store not found")
        except:
            abort(404, message="Invalid data received!")

    @store_blp.arguments(StoreSchema)
    def put(self, store_data):
        try:
            store = StoreModel.query.get(store_data["id"])
            print(store)
            if store:
                store.name = store_data["name"]
                db.session.add(store)
                db.session.commit()
                return {"message": "Store updated!"}
            else:
                abort(404, message="Store not found!")
        except:
            abort(404, message="Invalid data received!")
    


        
