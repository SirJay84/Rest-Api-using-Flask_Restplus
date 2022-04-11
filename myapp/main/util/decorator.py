from functools import wraps
from flask import request
from flask_jwt_extended import get_jwt

def jwt_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        access_token=None
        if 'Authorization'in request.headers:
            access_token=request.headers.get('Authorization')
        if not access_token:
            return {'message':'Token is missing.'},401
        try:
            payload=jwt.decode(access_token,key)
            current_user=UserModel.query.filter_by(public_id=data['public_id']).first()
        except:
            return{'message':'Token is invalid.'},401

        return f(current_user,*args,**kwargs)

    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        claims=get_jwt()
        is_admin=claims['admin']
        if is_admin==True:
            return f(*args,**kwargs)
        else:
            return{'message':'You cannot perform that function.'},401

    return decorated


