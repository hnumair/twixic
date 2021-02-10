from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

@app.route('/')
def hello():
    return 'Welcome to twixic!'

