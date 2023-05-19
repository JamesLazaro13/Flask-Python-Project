from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func 

class User_Info(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    monthlyIncome = database.Column(database.Integer)
    date = database.Column(database.DateTime(timezone=True), default=func.now())
    user_id = database.Column(database.Integer, database.ForignKey('user.id'))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(75), unique=True)
    password = database.Column(database.String(30))
    firstName = database.Column(database.String(30))
    user_info = database.relationship('User_Info')