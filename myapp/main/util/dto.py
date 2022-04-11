from flask_restplus import Namespace,fields

class UserDto():
    api=Namespace('user',description='User related operations.')
    user=api.model('user_details',{
        'email':fields.String(required=True,description='user email address'),
        'username':fields.String(required=True,description='user username'),
        'password':fields.String(required=True,description='user password')
    })

class AuthDto():
    api=Namespace('auth',description='Authentication related Operations.')
    user_auth=api.model('auth_details',{
        'email':fields.String(required=True,description='the email address'),
        'password':fields.String(required=True,description='the user password')
    })

class CustomerDto():
    api=Namespace('customer',description='Customer related Operations.')
    customer=api.model('customer_details',{
        'first_name':fields.String(required=True,description='customer first_name'),
        'last_name':fields.String(required=True,description='customer last_name'),
        'address':fields.String(required=True,description='customer address'),
        'city':fields.String(required=True,description='customer city'),
        'email':fields.String(required=True,description='customer email'),
        'phone_number':fields.String(required=True,description='customer phone_number')
    })

class OrderDto():
    api=Namespace('order',description='Order related Operations.')
    order=api.model('order_details',{
        'coupon_code':fields.String(required=True,description='order coupon_code'),
        'customer_id':fields.String(required=True,description='order customer_id')
    })

class ProductDto():
    api=Namespace('product',description='Product related Operations.')
    product=api.model('product_details',{
        'product_name':fields.String(required=True,description='product_name'),
        'product_category':fields.String(required=True,description='product_category'),
        'product_brand':fields.String(required=True,description='product_brand'),
        'product_size':fields.String(required=True,description='product_size'),
        'product_color':fields.String(required=True,description='product_color'),
        'product_price':fields.String(required=True,description='product_price')
    })