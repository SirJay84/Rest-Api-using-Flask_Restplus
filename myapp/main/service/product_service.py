from myapp.main.model.product import ProductModel
from myapp.main import db


def create_product(data):
        new_product=ProductModel(
            product_name=data['product_name'],
            product_category=data['product_category'],
            product_brand=data['product_brand'],
            product_size=data['product_size'],
            product_color=data['product_color'],
            product_price=data['product_price']        
        )
        db.session.add(new_product)
        db.session.commit()

        return {'status':'success','message':'Product created successfully.'}
    
def get_all_products(current_user):
    products=ProductModel.query.all()
    product_list=[]
    for product in products:
        product_details={
            'product_name':product.product_name,
            'product_category':product.product_category,
            'product_brand':product.product_brand,
            'product_size':product.product_size,
            'product_color':product.product_color,
            'product_price':product.product_price
        }
        product_list.append(product_details)

    return {'products':product_list}

def get_one_product(id):
    product=ProductModel.query.filter_by(id=id).first()
    if not product:
        return {'message':'Product not found.'}
    product_details={
        'product_name':product.product_name,
        'product_category':product.product_category,
        'product_brand':product.product_brand,
        'product_size':product.product_size,
        'product_color':product.product_color,
        'product_price':product.product_price
    }

    return {'product':product_details}

def update_product(id):
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

    return {'message':'Product has been updated.'}

def delete_product(id):
    product=ProductModel.query.filter_by(id=id).first()
    if not product:
        return {'message':'Product not found.'}
    else:
        db.session.delete(product)
        db.session.commit()
    
    return {'message':'Product has been deleted.'}



