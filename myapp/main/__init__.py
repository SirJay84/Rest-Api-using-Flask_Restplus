from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from myapp.main.config import app_config
from myapp.main.commands import create_database
from datetime import timedelta
from flask_jwt_extended import JWTManager

""" Initialize sqlalchemy"""
db=SQLAlchemy()

""" Initialize bcrypt"""
flask_bcrypt=Bcrypt()

jwt=JWTManager()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.cli.add_command(create_database)
    app.config['JWT_SECRET_KEY']='59c3d0340f4943f9bfbe15e2e523e3be'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(minutes=30)
    app.config['JWT_REFRESH_TOKEN_EXPIRES']=timedelta(days=30)
    jwt.init_app(app)
    

    return app




