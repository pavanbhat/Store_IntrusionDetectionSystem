from flask_sqlalchemy import SQLAlchemy

user_db = SQLAlchemy()


class ProductList(user_db.Model):
    __tablename__ = 'products'
    __bind_key__ = 'products'
    uid = user_db.Column(user_db.TEXT, primary_key=True)
    name = user_db.Column(user_db.TEXT)
    price = user_db.Column(user_db.TEXT)
    category = user_db.Column(user_db.String(120), unique=True)

    def __init__(self, uid, name, price, category):
        self.uid = uid
        self.name = name
        self.price = price
        self.category = category
