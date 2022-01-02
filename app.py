from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
import json
import http
from resources.items import Item, ItemList
from resources.users import UserRegister
from resources.stores import Store, StoreList 
app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item , "/item/<string:name>")
api.add_resource(ItemList , "/items")
api.add_resource(UserRegister , "/user")
api.add_resource(Store , "/store/<string:name>")
api.add_resource(StoreList , "/stores")


#api.add_resource(Item , "/items")


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)