from myapp.main import db
from myapp.main.model.blacklist import BlacklistToken

def save_token(token):
    """Mark the token as blacklisted"""
    blacklist_token=BlacklistToken(token=access_token)
    try:
        """Insert the token"""
        db.session.add(blacklist_token)
        db.session.commit()

        return{'status':'success','message':'Successfully logged out.'}

    except Exception as e:

        return {'status':'fail','message':e}