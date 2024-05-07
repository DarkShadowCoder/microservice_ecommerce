from flask import flash, Flask, render_template, request, jsonify,session
import utils
from sqlalchemy import exc
import datetime


app = Flask(__name__)

conn = utils.get_db_connection()
cur = conn.cursor()

@app.route('/products', methods=["POST"])
def add_products():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    name = post_data.get('name')
    category = post_data.get('category')
    price = post_data.get('price')
    description = post_data.get('description')
    image_path = post_data.get('image_path')

    try:
        product = utils.get_product_by_name(name)
        if not product:
            utils.set_product(name,category,price,description,image_path)
            response_object['status'] = 'success'
            response_object['message'] = f'{name} was created'
            return jsonify(response_object),201
        
        else:
            response_object["message"] = "Sorry. That username or email already exists"
            return jsonify(response_object),400
    except exc.IntegrityError as e:
        session.clear()
        return jsonify(response_object),400

@app.route('/products/<int:product_id>', methods=["GET"])
def get_single_product(product_id):
    """Get single product details"""
    response_object = {
        'status': 'fail',
        'message':'Product does not exist'
    }
    try:
        product = utils.get_product(product_id)
        if not product:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':product[0],
                    'name':product[1],
                    'category':product[2],
                    'price': product[3],
                    'description': product[4],
                    'image_path': product[6],
                    'date' : str(product[5])
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/products',methods={'GET'})
def get_all_products():
    """Get all products"""
    response_object = {
        'status':'success',
        'data':{
            'users':[utils.product_json(product) for product in utils.get_all_products()]
        }
    }
    return jsonify(response_object), 200

@app.route('/products/delete/<int:product_id>', methods=["POST"])
def delete_product(product_id):
    """Delete product"""
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    else:
        try:
            utils.delete_product(id=product_id)
            response_object["message"] = "Product deleted sucessfully!"
            return jsonify(response_object),200
        except exc.IntegrityError as e:
            response_object["message"] = f"Failled to delete Product with id: {product_id}"
            response_object["status"] = "fail"
            return jsonify(response_object),400


#### ----------- Category Routes ------------ ####
@app.route('/category', methods=["POST"])
def add_category():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    name = post_data.get('name')

    try:
        category = utils.get_category(name)
        if not category:
            utils.set_category(name)
            response_object['status'] = 'success'
            response_object['message'] = f'{name} was created'
            return jsonify(response_object),201
        
        else:
            response_object["message"] = "Sorry. That category already exists"
            return jsonify(response_object),400
    except exc.IntegrityError as e:
        session.clear()
        return jsonify(response_object),400

@app.route('/category/<string:name>', methods=["GET"])
def get_single_category(name):
    """Get single category details"""
    response_object = {
        'status': 'fail',
        'message':'Category does not exist'
    }
    try:
        category = utils.get_category(name=name)
        if not category:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'name':category[0]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/category',methods=['GET'])
def get_all_categories():
    """Get all categories """
    response_object = {
        'status':'success',
        'data':{
            'categories':[utils.category_json(category) for category in utils.get_all_categories()]
        }
    }
    print(utils.get_all_categories())
    return jsonify(response_object), 200

@app.route('/category/delete/<string:category_name>', methods=["POST"])
def delete_category(category_name):
    """Delete category"""
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    else:
        try:
            utils.delete_product(id=category_name)
            response_object["message"] = "Category deleted successfully!"
            return jsonify(response_object),200
        except exc.IntegrityError as e:
            response_object["message"] = f"Failled to delete category with name: {category_name}"
            response_object["status"] = "fail"
            return jsonify(response_object),400
