from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////twixic'

db = SQLAlchemy(app)
login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

@app.route('/')
def hello():
    return 'Welcome to twixic!'

