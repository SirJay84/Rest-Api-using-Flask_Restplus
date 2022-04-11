from flask import Blueprint
from flask_restplus import Api
from myapp.main.controller.user_controller import api as user_ns
from myapp.main.controller.auth_controller import api as auth_ns
from myapp.main.controller.customer_controller import api as customer_ns
from myapp.main.controller.order_controller import api as order_ns
from myapp.main.controller.product_controller import api as product_ns

blueprint=Blueprint('api', __name__)

api=Api(blueprint,
        title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
        Version='1.0',
        description='a boiler plate for flask restplus web service'
        )

api.add_namespace(user_ns,path='/user')
api.add_namespace(auth_ns)
api.add_namespace(customer_ns,path='/customer')
api.add_namespace(order_ns,path='/order')
api.add_namespace(product_ns,path='/product')