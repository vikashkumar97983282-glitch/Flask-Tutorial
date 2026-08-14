from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# create database object globally
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'MY-SECRET-KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICTIONS'] = False

    db.__init__(app)

    from app.routes import auth_bp
    from app.routes import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app