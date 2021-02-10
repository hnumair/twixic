from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from flask_migrate import Migrate
from sqlalchemy.sql import func

from backend import db

ma = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primarykey=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password_hash = db.Column(db.String())

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primarykey=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created = db.Column(db.DateTime(), nullable=False, default=func.now())
    body = db.Column(db.String(240), nullable=False)


