from myapp.main import db
import datetime

order_product=db.Table('order_product',
    db.Column('order_id',db.Integer,db.ForeignKey('order.id'),primary_key=True),
    db.Column('product_id',db.Integer,db.ForeignKey('product.id'),primary_key=True)
)

class OrderModel(db.Model):
    __tablename__='order'
    
    id=db.Column(db.Integer,primary_key=True)
    order_date=db.Column(db.DateTime,nullable=False,default=datetime.datetime.utcnow())
    shipped_date=db.Column(db.DateTime)
    delivered_date=db.Column(db.DateTime)
    coupon_code=db.Column(db.String(50))
    customer_id=db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=False)

    products=db.relationship('ProductModel',secondary='order_product')

    def __init__(self,order_date,shipped_date,delivered_date,coupon_code,customer_id):
        self.order_date=datetime.datetime.utcnow()
        self.shipped_date=datetime.datetime.utcnow()
        self.delivered_date=datetime.datetime.utcnow()
        self.coupon_code=coupon_code
        self.customer_id=customer_id

    def __repr__(self):

        return "< OrderModel'{}'>".format(self.id)

