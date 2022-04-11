from myapp.main import db,flask_bcrypt
from myapp.main.model.blacklist import BlacklistToken
from myapp.main.config import key
import datetime
import jwt


class UserModel(db.Model):
    
    __tablename__ = 'users'

    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.String(100),unique=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    registered_on=db.Column(db.DateTime,nullable=False)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password_hash=db.Column(db.String(100),nullable=False)
    is_admin=db.Column(db.Boolean,default=False)

    @property
    def password(self):
        raise AttributeError('password:write-only field')

    @password.setter
    def password(self,password):
        self.password_hash=flask_bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return flask_bcrypt.check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "<UserModel '{}'>".format(self.username)

    @staticmethod
    def encode_access_token(self,public_id):
        """Generates access_token"""
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30),
                'iat':datetime.datetime.utcnow(),
                'sub':public_id
            }

            return jwt.encode(payload,key,algorithm='HS256')

        except Exception as e:

            return e

    @staticmethod
    def decode_access_token(access_token):
        """Decodes access_token"""
        try:
            payload=jwt.decode(access_token,key)
            is_blacklisted_token=BlacklistToken.check_blacklist(access_token)
            if is_blacklisted_token:
                return 'Token blacklisted.Please login again.'
            else:
                return payload ['sub']

        except jwt.ExpiredSignatureError:
            return 'Signature expired.Please login again.'

        except jwt.InvalidTokenError:
            return 'Invalid token.Please login again.'


 