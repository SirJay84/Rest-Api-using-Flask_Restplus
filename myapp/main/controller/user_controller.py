from flask import request
from flask_restplus import Resource
from myapp.main.util.dto import UserDto
from myapp.main.service.user_service import create_user,get_all_users,get_one_user,update_user,delete_user
from myapp.main.model.user import UserModel
from myapp.main import db
from flask_jwt_extended import jwt_required
from myapp.main.util.decorator import admin_required

api=UserDto.api
user=UserDto.user

authorizations={
    'Bearer Auth':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

@api.route('/')
class UserList(Resource):
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_list_with(user,envelope='user_data')
    @jwt_required()
    @admin_required
    def get(current_user):
        """List of registered users"""
        users=UserModel.query.all()

        return users  

    @api.doc('create_user')
    @api.response(201,'User created successfully.')
    @api.expect(user,validate=True)
    def post(current_user):
        """Create new user"""
        data=request.json
        
        return create_user(data=data)

@api.route('/<public_id>')
@api.param('public_id','The user identifier.')
@api.response(404,'User not found.')
class User(Resource):
    @api.doc('update a user')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.expect(user)
    @jwt_required()
    @admin_required
    def put(current_user,public_id):
        """Update a user given its identifier"""
        user=UserModel.query.filter_by(public_id=public_id).first()
        if not user:
            return {'message':'User not found.'}
        
        user.is_admin=True
        
        db.session.commit()
            
        return {'message':'User updated.'}

    @api.doc('delete a user')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required()
    @admin_required
    def delete(current_user,public_id):
        """Delete a user given its identifier"""
        user=UserModel.query.filter_by(public_id=public_id).first()
        if not user:
            return {'message':'User not found.'}
        else:
            db.session.delete(user)
            db.session.commit()
            
        return {'message':'User deleted.'}

    @api.doc('get a user')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_with(user)
    @jwt_required()
    @admin_required
    def get(current_user,public_id):
        """Get a user given its identifier"""
        user=UserModel.query.filter_by(public_id=public_id).first()
        if not user:
            return {'message':'User not found'}
        else:
            return user


    
 