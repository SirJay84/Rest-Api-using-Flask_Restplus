from myapp.main.model.user import UserModel
from myapp.main.service.blacklist_service import save_token
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity,get_jwt
import datetime
from myapp.main import db
from myapp.main.model.blacklist import BlacklistToken

class Auth:
    @staticmethod
    def login_user(data):
        """Fetch user data""" 
        user=UserModel.query.filter_by(email=data.get('email')).first()
        if user and user.check_password(data.get('password')):
            additional_claims={'admin':user.is_admin}
            access_token=create_access_token(identity=user.public_id,fresh=True,additional_claims=additional_claims)
            refresh_token=create_refresh_token(identity=user.public_id)
            return {
                'status':'success',
                'message':'Successfully logged in.',
                'access_token':access_token,
                'refresh_token':refresh_token
            },200

        else:
            return {'status':'fail','message':'email or password does not match.'},401

    @staticmethod
    def logout_user(data):
        jti=get_jwt()['jti']
        now=datetime.datetime.utcnow()
        db.session.add(BlacklistToken(jti=jti,created_at=now))
        db.session.commit()

        return {'message':'Token blacklisted.'}

    @staticmethod
    def get_logged_in_user():
        """Access the identity of current_user with get_jwt_identity"""
        current_user=get_jwt_identity()

        return {'logged_in_as':current_user},200