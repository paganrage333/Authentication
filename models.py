from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    username = db.Column(db.String(20),
                         primary_key=True,
                         unique=True,
                         nullable=False)
    password = db.Column(db.Text, 
                         nullable=False)

    email = db.Column(db.String(50), 
                      unique=True, 
                      nullable=False)
    first_name = db.Column(db.String(30), 
                           nullable=False)
    last_name = db.Column(db.String(30), 
                          nullable=False)


def connect_db(app):
    db.app = app
    db.init_app(app)
