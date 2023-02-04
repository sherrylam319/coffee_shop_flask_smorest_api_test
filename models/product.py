from db import db

class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False, unique=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False, unique=False)
    store = db.relationship("StoreModel", back_populates="product")

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id





