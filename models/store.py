from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    product = db.relationship("ProductModel", back_populates="store")

    def __init__(self, location, name):
        self.location = location
        self.name = name


