import uuid
import datetime
from myapp.main.model.user import UserModel
from myapp.main import db,flask_bcrypt
from flask_jwt_extended import create_access_token,create_refresh_token

def create_user(data):
    user=UserModel.query.filter_by(email=data['email']).first()
    if not user:
        new_user=UserModel(public_id=str(uuid.uuid4()),email=data['email'],username=data['username'],registered_on=datetime.datetime.utcnow(),password=data['password'],is_admin=False)
        db.session.add(new_user)
        db.session.commit()

        return generate_token(new_user)

    else:
        return {'status':'fail','message':'User already exists.Please Login!'}

def get_all_users():
    users=UserModel.query.all()
    user_list=[]
    for user in users:
        user_data={
            'public_id':user.public_id,
            'email':user.email,
            'username':user.username,
            'password_hash':user.password_hash,
            'registered_on':datetime.datetime.utcnow(),
            'is_admin':user.is_admin
        }
        user_list.append(user_data)

    return {'users':user_list}  

def get_one_user(public_id):
    user=UserModel.query.filter_by(public_id=public_id).first()
    if not user:
        return{'message':'User not found!'}
    user_data={
        'public_id':user.public_id,
        'email':user.email,
        'username':user.username,
        'password_hash':user.password_hash,
        'registered_on':datetime.datetime.utcnow(),
        'is_admin':user.is_admin
    }

    return {'user':user_data}

def update_user(public_id):
    user=UserModel.query.filter_by(public_id=public_id).first()
    if not user:
        return {'message':'User not found!'}
    
    user.is_admin=True
    db.session.commit()
     
    return {'message':'User has been updated!'}

def delete_user(public_id):
    user=UserModel.query.filter_by(public_id=public_id).first()
    if not user:
        return {'message':'User not found!'}
    else:
        db.session.delete(user)
        db.session.commit()
    
    return {'message':'User has been deleted!'}

def generate_token(user):
    access_token=create_access_token(identity=user.public_id,fresh=True)
    refresh_token=create_refresh_token(identity=user.public_id)
    return{
        'status':'success',
        'message':'Successfully registered.',
        'access_token':access_token,
        'refresh_token':refresh_token
    },201


    