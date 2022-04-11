from flask import request
from flask_restplus import Resource
from myapp.main.model.order import OrderModel
from myapp.main.util.dto import OrderDto
from myapp.main.service.order_service import create_an_order,get_all_orders,get_an_order,update_an_order,delete_an_order
from myapp.main import db
from flask_jwt_extended import jwt_required


api=OrderDto.api
order=OrderDto.order

authorizations={
    'Bearer Auth':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

@api.route('/')
class OrderList(Resource):
    @api.doc('Get all orders')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_list_with(order,envelope='order_details')
    @jwt_required()
    def get(current_user):
        """List all orders"""
        orders=OrderModel.query.all()

        return orders

    @api.doc('Create an order')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.response(201,'Order created successfully.')
    @api.expect(order,validate=True)
    @jwt_required()
    def post(current_user):
        """Create new order"""
        data=request.json

        return create_an_order(data=data)

@api.route('/<id>')
@api.param('id','The order identifier.')
@api.response(404,'Order not found.')
class Order(Resource):
    @api.doc('Update an order')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.expect(order)
    @jwt_required()
    def put(current_user,id):
        """Update an order given its identifier"""
        data=request.json
        order=OrderModel.query.filter_by(id=id).first()
        if not order:
            return {'message':'Order not found.'}
        else:
            order.coupon_code=data['coupon_code']
            order.customer_id=data['customer_id']

            db.session.commit()

        return {'message':'Order updated.'}

    @api.doc('Delete an order')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required()
    def delete(current_user,id):
        """Delete an order given its identifier"""
        order=OrderModel.query.filter_by(id=id).first()
        if not order:
            return {'message':'Order not found.'}
        else:
            db.session.delete(order)
            db.session.commit()
        
        return {'message':'Order deleted.'}

    @api.doc('Get an order')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_with(order)
    @jwt_required()
    def get(current_user,id):
        """Get an order given its identifier"""
        order=OrderModel.query.filter_by(id=id).first()
        if not order:
            return {'message':'Order not found.'}
        else:
            return order