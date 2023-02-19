from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, get_jwt

from db import db
from models import ProductModel
from schemas import ProductSchema, ProductUpdateSchema


blp = Blueprint("products", __name__, description="Operations on products")


@blp.route("/product/<int:product_id>")
class Products(MethodView):
    @blp.response(200, ProductSchema)
    def get(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product

    @jwt_required(fresh=True)
    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)

        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}

    @jwt_required(fresh=False)
    @blp.arguments(ProductUpdateSchema)
    @blp.response(200, ProductSchema)
    def put(self, product_data, product_id):
        product = ProductModel.query.get(product_id)
        if product:
            product.price = product_data["price"]
            product.name = product_data["name"]
            product.store_id = product_data["store_id"]
        else:
            product = ProductModel(id=product_id, **product_data)

        db.session.add(product)
        db.session.commit()

        return product


@blp.route("/product")
class ProductList(MethodView):

    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, product_data):
        product = ProductModel(**product_data)

        try:
            db.session.add(product)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item.")
        
        return product



