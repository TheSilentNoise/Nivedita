from app import db
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

############ models

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(500))
    user_email = db.Column(db.String(100),unique=True)
    user_phoneno = db.Column(db.String(100))
    user_password = db.Column(db.String(256))
    date_created = db.Column(db.DateTime)

    def is_authenticated(self):
        return False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(500))
    course_url = db.Column(db.String(500))
    child = relationship("User_Course")


class User_Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer)
    course_id =db.Column(db.Integer,ForeignKey('courses.id'))
    date_created = db.Column(db.DateTime)











