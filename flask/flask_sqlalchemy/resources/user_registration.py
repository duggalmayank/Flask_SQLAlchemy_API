import sqlite3
from flask_restful import Resource, reqparse
from models.user import User

class UserRegistration(Resource):

     parser = reqparse.RequestParser()
     parser.add_argument('username', type=str, required=True, help="This field can not be left blank!")
     parser.add_argument('password', type=str, required=True, help='This field can not be left blank!')

     def post(self):
          data = UserRegistration.parser.parse_args()

          if User.find_by_username(data['username']):
               return {"message": "username already in use"}, 400

          user = User(**data)
          user.save_to_db()

          return {"message": "User created"}, 201
