class Config():
    """Parent Configuration class"""
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///db.ecommerce'
    SECRET_KEY='2c2d114fee1140979418b55561f1a9c7'

class DevelopmentConfig(Config):
    """Development Configuration class"""
    DEBUG=True

app_config={'development':DevelopmentConfig}

key=Config.SECRET_KEY