from myapp.main.model.order import OrderModel
from myapp.main import db
import datetime


def create_an_order(data):
        new_order=OrderModel(
            order_date=datetime.datetime.utcnow(),
            shipped_date=datetime.datetime.utcnow(),
            delivered_date=datetime.datetime.utcnow(),
            coupon_code=data['coupon_code'],
            customer_id=data['customer_id']
        )
        db.session.add(new_order)
        db.session.commit()

        return {'status':'success','message':'Order created successfully.'}


def get_all_orders():
    orders=OrderModel.query.all()
    order_list=[]
    for order in orders:
        order_details={
        'order_date':datetime.datetime.utcnow(),
        'shipped_date':datetime.datetime.utcnow(),
        'delivered_date':datetime.datetime.utcnow(),
        'coupon_code':order.coupon_code,
        'customer_id':order.customer_id
    }
    order_list.append(order_details)

    return {'orders':order_list}

def get_an_order(id):
    order=OrderModel.query.filter_by(id=id).first()
    if not order:
        return{'message':'Order not found.'}
    order_details={
        'order_date':datetime.datetime.utcnow(),
        'shipped_date':datetime.datetime.utcnow(),
        'delivered_date':datetime.datetime.utcnow(),
        'coupon_code':order.coupon_code,
        'customer_id':order.customer_id
    }

    return {'order':order_details}

def update_an_order(id):
    order=OrderModel.query.filter_by(id=id).first()
    if not order:
        return {'message':'Order not found.'}
    else:
        order.coupon_code=data['coupon_code'],
        order.customer_id=data['customer_id']

        db.session.commit()

    return {'message':'Order has been updated.'}

def delete_an_order(id):
    order=OrderModel.query.filter_by(id=id).first()
    if not order:
        return {'message':'Order not found.'}
    else:
        db.session.delete(order)
        db.session.commit()

    return {'message':'Order has been deleted.'}


