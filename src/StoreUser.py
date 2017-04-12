from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

user_db = SQLAlchemy()


class StoreUser(user_db.Model):
    __tablename__ = 'store_users'
    __bind_key__ = 'store_users'
    uid = user_db.Column(user_db.Integer, primary_key=True)
    email = user_db.Column(user_db.String(60), unique=True)
    username = user_db.Column(user_db.String(20), unique=True)
    password = user_db.Column(user_db.TEXT)

    def __init__(self, email, username, password):
        self.email = email.lower()
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
