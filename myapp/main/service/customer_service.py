from myapp.main.model.customer import CustomerModel
from myapp.main import db



def create_customer(data):
    customer=CustomerModel.query.filter_by(email=data['email']).first()
    if not customer:
        new_customer=CustomerModel(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            city=data['city'], 
            email=data['email'],
            phone_number=data['phone_number']
        )
        db.session.add(new_customer)
        db.session.commit()

        return {'status':'success','message':'customer created successfully.'}

    else:
        return {'status':'fail','message':'customer already exists.'}

def get_all_customers():
    customers=CustomerModel.query.all()
    customer_list=[]
    for customer in customers:
        customer_data={
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'address':customer.address,
            'city':customer.city,
            'email':customer.email,
            'phone_number':customer.phone_number
        }
        customer_list.append(customer_data)

    return {'customers':customer_list}

def get_one_customer(id):
    customer=CustomerModel.query.filter_by(id=id).first()
    if not customer:
        return {'message':'customer not found.'}
    customer_data={
        'first_name':customer.first_name,
        'last_name':customer.last_name,
        'address':customer.address,
        'city':customer.city,
        'email':customer.email,
        'phone_number':customer.phone_number
    }

    return {'customer':customer_data}

def delete_customer(id):
    customer=CustomerModel.query.filter_by(id=id).first()
    if not customer:
        return {'message':'customer not found.'}
    else:
        db.session.delete(customer)
        db.session.commit()

    return {'message':'Customer has been deleted.'}

def update_customer(id):
    customer=CustomerModel.query.filter_by(id=id).first()
    if not customer:
        return {'message':'customer not found.'}
    else:
        customer.first_name=data['first_name']
        customer.last_name=data['last_name']
        customer.address=data['address']
        customer.city=data['city']
        customer.email=data['email']
        customer.phone_number=data['phone_number']
        
        db.session.commit()

    return{'message':'customer has been updated.'}












