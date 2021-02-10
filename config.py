import os

SQLALCHEMY_DATABASE_URI = "postgresql:///twixic"
SECRET_KEY = os.urandom(32)
SQLALCHEMY_TRACK_MODIFICATIONS = True

