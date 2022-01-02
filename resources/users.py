from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be blank'
    )

    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be blank'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        username = data.get('username')

        user = UserModel(username=data.get('username'), password=data.get('password'))
        if UserModel.find_by_username(username=username):
            return ({'message': f'User with {username} already exists'}), 400
        else:
            user.save_to_db()
        
        return user.json(), 200
    
    # def delete():
    #     data = UserRegister.parser.parse_args()

    #     username = data.get('username')
    #     if not UserModel.find_by_username(username):
    #         return ({'message': f'User with {username} does not exists'}), 404
    #     else:
    #         UserModel.delete_from_db()
        
    #     return UserModel.json(), 200
        
        
