from app import db
from flask_login import UserMixin

############ models

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(500))
    user_email = db.Column(db.String(100),unique=True)
    user_phoneno = db.Column(db.String(100))
    user_password = db.Column(db.String(256))
    creation_time = db.Column(db.DateTime)

    def is_authenticated(self):
        return False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
