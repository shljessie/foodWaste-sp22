from sys import meta_path
from . import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func 
from datetime import datetime
from dataclasses import dataclass
import time


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@dataclass
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    foodWaste = db.relationship('UserFoodWaste')
    clicks = db.relationship('UserClicks')

@dataclass
class UserFoodWaste(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=datetime.now)
    fruit= db.Column(db.Integer)
    veggies = db.Column(db.Integer)
    dairy = db.Column(db.Integer)
    meat = db.Column(db.Integer)
    poultry = db.Column(db.Integer)
    fish_seafood = db.Column(db.Integer) 
    takeout = db.Column(db.Integer) 
    other = db.Column(db.Integer) 
    js_date = db.Column(db.Integer)

class UserClicks(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=datetime.now)
    foodwCLICK = db.Column(db.Integer)
    monwCLICK = db.Column(db.Integer)
    progCLICK = db.Column(db.Integer)
    gomCLICK = db.Column(db.Integer)

