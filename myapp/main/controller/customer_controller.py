from flask import request
from flask_restplus import Resource
from myapp.main.util.dto import CustomerDto
from myapp.main.service.customer_service import create_customer,get_all_customers,get_one_customer,update_customer,delete_customer
from myapp.main import db
from myapp.main.model.customer import CustomerModel
from flask_jwt_extended import jwt_required

api=CustomerDto.api
customer=CustomerDto.customer

authorizations={
    'Bearer Auth':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

@api.route('/')
class CustomerList(Resource):
    @api.doc('Get_all_customers')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_list_with(customer,envelope='customer_data')
    @jwt_required()
    def get(current_user):
        """List all customers"""
        customers=CustomerModel.query.all()

        return customers

    @api.doc('Create_customer')
    @api.response(201,'Customer created successfully.')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.expect(customer,validate=True)
    @jwt_required()
    def post(current_user):
        """Create new customer"""
        data=request.json

        return create_customer(data=data)

@api.route('/<id>')
@api.param('id','The customer identifier.')
@api.response(404,'Customer not found.')
class Customer(Resource):
    @api.doc('update_customer')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.expect(customer)
    @jwt_required()
    def put(current_user,id):
        """Update a customer given its identifier"""
        data=request.json
        customer=CustomerModel.query.filter_by(id=id).first()
        if not customer:
            return {'message':'Customer not found.'}
        else:
            customer.first_name=data['first_name']
            customer.last_name=data['last_name']
            customer.address=data['address']
            customer.city=data['city']
            customer.email=data['email']
            customer.phone_number=data['phone_number']
        
            db.session.commit()

        return{'message':'Customer updated.'}

    @api.doc('delete_customer')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @jwt_required()
    def delete(current_user,id):
        """Delete a customer given its identifier"""
        customer=CustomerModel.query.filter_by(id=id).first()
        if not customer:
            return {'message':'Customer not found.'}
        else:
            db.session.delete(customer)
            db.session.commit()

        return {'message':'Customer deleted.'}

    @api.doc('get_one_customer')
    @api.doc(params={'Authorization':{'in':'header','description':'Authorization token'}})
    @api.marshal_with(customer)
    @jwt_required()
    def get(current_user,id):
        """Get a customer given its identifier"""
        customer=CustomerModel.query.filter_by(id=id).first()
        if not customer:
            return{'message':'Customer not found.'}
        else:
            return customer



        


