from myapp.main import db
import datetime

class BlacklistToken(db.Model):

    __tablename__ = 'blacklist_tokens'

    id=db.Column(db.Integer,primary_key=True)
    jti=db.Column(db.String(100),unique=True,nullable=False)
    created_at=db.Column(db.DateTime,nullable=False)

    def __init__(self,jti,created_at):
        self.jti=jti
        self.created_at=datetime.datetime.utcnow()

    def __repr__(self):
        return "<BlacklistToken '{}'>".format(self.jti)

    @staticmethod
    def check_blacklist(access_token):
        """Check whether access_token is blacklisted"""
        resp=BlacklistToken.query.filter_by(jti=jti).first()
        if resp:
            return True
        else:
            return False




