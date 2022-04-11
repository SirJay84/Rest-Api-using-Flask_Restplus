from flask import request
from flask_restplus import Resource
from myapp.main.service.auth_helper import Auth
from myapp.main.util.dto import AuthDto
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
from myapp.main.util.decorator import admin_required

api=AuthDto.api
user_auth=AuthDto.user_auth

authorizations={
    'Bearer Auth':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(user_auth,validate=True)
    def post(self):
        """Login a user"""
        post_data=request.json

        return Auth.login_user(data=post_data)

@api.route('/logout')
class LogoutAPI(Resource):
    @api.doc('Logout user')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required()
    def post(self):
        """Logout a user"""
        auth_header=request.headers.get('Authorization')

        return Auth.logout_user(data=auth_header)

@api.route('/refresh')
class TokenRefresh(Resource):
    @api.doc('Refresh token')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required(refresh=True)
    def post(current_user):
        current_user=get_jwt_identity()
        new_token=create_access_token(identity=current_user,fresh=False)
        return {'access_token':new_token},200
