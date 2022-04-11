from flask import request
from flask_restplus import Resource
from myapp.main.service.product_service import create_product,get_all_products,get_one_product,update_product,delete_product
from myapp.main.util.dto import ProductDto
from myapp.main import db
from myapp.main.model.product import ProductModel
from flask_jwt_extended import jwt_required


api=ProductDto.api
product=ProductDto.product

authorizations={
    'Bearer Auth':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

@api.route('/')
class ProductList(Resource):
    @api.doc('Get all products')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_list_with(product,envelope='product_details')
    @jwt_required()
    def get(current_user):
        """List all Products"""
        products=ProductModel.query.all()

        return products

    @api.doc('create a product')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.response(201,'Product created successfully.')
    @api.expect(product,validate=True)
    @jwt_required()
    def post(current_user):
        """Create new product"""
        data=request.json

        return create_product(data=data)

@api.route('/<id>')
@api.param('id','The Product identifier.')
@api.response(404,'Product not found.')
class Product(Resource):
    @api.doc('Update a product')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.expect(product)
    @jwt_required()
    def put(current_user,id):
        """Update a product given its identifier"""
        data=request.json
        product=ProductModel.query.filter_by(id=id).first()
        if not product:
            return {'message':'Product not found.'}
        else:
            product.product_name=data['product_name']
            product.product_category=data['product_category']
            product.product_brand=data['product_brand']
            product.product_size=data['product_size']
            product.product_color=data['product_color']
            product.product_price=data['product_price']

            db.session.commit()

        return {'message':'Product updated.'}

    @api.doc('delete a product')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required()
    def delete(current_user,id):
        """Delete a product given its identifier"""
        product=ProductModel.query.filter_by(id=id).first()
        if not product:
            return {'message':'Product not found.'}
        else:
            db.session.delete(product)
            db.session.commit()
        return {'message':'Product deleted.'}

    @api.doc('Get a product')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_with(product)
    @jwt_required()
    def get(current_user,id):
        """Get a product given its identifier"""
        product=ProductModel.query.filter_by(id=id).first()
        if not product:
            return {'message':'Product not found.'}
        else:
            return product




