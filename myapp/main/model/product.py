from myapp.main import db



class ProductModel(db.Model):
    __tablename__ = 'product'

    id=db.Column(db.Integer,primary_key=True)
    product_name=db.Column(db.String(50),nullable=False,unique=True)
    product_category=db.Column(db.String(50),nullable=False)
    product_brand=db.Column(db.String(20),nullable=False)
    product_size=db.Column(db.Integer,nullable=False)
    product_color=db.Column(db.String(20),nullable=False)
    product_price=db.Column(db.Integer,nullable=False)
    
    def __init__(self,product_name,product_category,product_brand,product_size,product_color,product_price):
        self.product_name=product_name
        self.product_category=product_category
        self.product_brand=product_brand
        self.product_size=product_size
        self.product_color=product_color
        self.product_price=product_price
    
    
    def __repr__(self):
        return "< ProductModel '{}'>".format(self.id)

