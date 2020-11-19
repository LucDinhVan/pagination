import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserLogin, UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Không lưu vào db ngay khi object bị thay đổi
app.secret_key = 'jose'
# app.config['JWT_SECRET_KEY'] = 'Lucdeptrai'
api = Api(app)

@app.before_first_request
def create_tables():
    """
    Tạo db trước tiên khi app chạy
    """
    db.create_all()

# app.config['JWT_AUTH_URL_RULE'] = '/login'
# # config JWT to expire within half an hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# # config JWT auth key name to be 'email' instead of default 'username'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
# jwt = JWT(app, authenticate, identity) # /auth

JWTManager(app)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>') 
api.add_resource(UserLogin, '/login')

if __name__ == "__main__":
    db.init_app(app)
    app.run(host="localhost", port=5000, debug=True)
