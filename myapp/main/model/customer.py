from myapp.main import db
#from myapp.main.model import order

class CustomerModel(db.Model):
    __tablename__ = 'customer'

    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    city=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(255),nullable=False,unique=True)
    phone_number=db.Column(db.String(10),nullable=False,unique=True)
    
    orders=db.relationship('OrderModel',backref='customer')

  
    
    def __init__(self,first_name,last_name,address,city,email,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.email=email
        self.phone_number=phone_number

    
    def __repr__(self):
        return "< CustomerModel '{}'>".format(self.id)



