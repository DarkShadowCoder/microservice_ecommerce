from flask import flash, Flask, render_template, request, jsonify,session
import utils
from sqlalchemy import exc


app = Flask(__name__)

conn = utils.get_db_connection()
cur = conn.cursor()

@app.route('/orders', methods=["POST"])
def add_order():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    username = post_data.get('username')
    cart_number = post_data.get('cart_number')

    try:
        utils.set_order(username,cart_number)
        response_object['status'] = 'success'
        response_object['bill'] = f'order was created'
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "Failled to create new order"
        return jsonify(response_object),400

@app.route('/orders/<int:order_id>', methods=["GET"])
def get_single_order(order_id):
    """Get single order details"""
    response_object = {
        'status': 'fail',
        'bill':'order does not exist'
    }
    try:
        order = utils.get_order(order_id)
        if not order:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':order[0],
                    'username':order[1],
                    'cart_number':order[2],
                    'status':order[3],
                    'date': order[4]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/orders',methods={'GET'})
def get_all_orders():
    """Get all orders"""
    response_object = {
        'status':'success',
        'data':{
            'orders':[utils.order_json(order) for order in utils.get_all_orders()]
        }
    }
    return jsonify(response_object), 200

@app.route('/orders/delete/<int:order_id>')
def delete_order(order_id):
    """Delete a order"""
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    try:
        utils.delete_order(order_id)
        response_object['bill'] = "order deleted successfully!"
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "order has not been deleted!"
        response_object["status"] = "fail"
        return jsonify(response_object),400



####################################################################
# ##############        REVIEWS ROUTES      ########################
####################################################################



@app.route('/reviews', methods=["POST"])
def add_review():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    order_id = post_data.get('order_id')
    rating = post_data.get('rating')
    product_id = post_data.get('product_id')
    review = post_data.get('review')

    try:
        utils.set_review(order_id,product_id,rating, review)
        response_object['status'] = 'success'
        response_object['bill'] = f'review was created'
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "Order post failled"
        session.clear()
        return jsonify(response_object),400

@app.route('/reviews/<int:review_id>', methods=["GET"])
def get_single_review(review_id):
    """Get single review details"""
    response_object = {
        'status': 'fail',
        'bill':'Review does not exist'
    }
    try:
        review = utils.get_review(review_id)
        if not review:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':review[0],
                    'order_id':review[1],
                    'product_id':review[2],
                    'rating':review[3],
                    'review':review[4],
                    'date': review[5]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/reviews',methods=['GET'])
def get_all_reviews():
    """Get all reviews"""
    response_object = {
        'status':'success',
        'data':{
            'reviews':[utils.review_json(review) for review in utils.get_all_reviews()]
        }
    }
    return jsonify(response_object), 200

@app.route('/reviews/delete/<int:review_id>')
def delete_review(review_id):
    """Delete a review"""
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    try:
        utils.delete_review(id=review_id)
        response_object['bill'] = "review deleted successfully!"
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "review has not been deleted!"
        response_object["status"] = "fail"
        return jsonify(response_object),400


####################################################################
# ##############        bills ROUTES      ########################
####################################################################


@app.route('/bills', methods=["POST"])
def add_bill():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    orders = post_data.get('order_id')

    try:
        utils.set_bill(orders)
        response_object['status'] = 'success'
        response_object['bill'] = f'bill was created'
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "bill post failled"
        return jsonify(response_object),400

@app.route('/bills/<int:bill_id>', methods=["GET"])
def get_single_bill(bill_id):
    """Get single bill details"""
    response_object = {
        'status': 'fail',
        'bill':'bill does not exist'
    }
    try:
        bill = utils.get_bill(bill_id)
        if not bill:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':bill[0],
                    'order_id':bill[1],
                    'bill':bill[2],
                    'date': bill[3]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/bills',methods=['GET'])
def get_all_bills():
    """Get all bills"""
    response_object = {
        'status':'success',
        'data':{
            'bills':[utils.bill_json(bill) for bill in utils.get_all_bills()]
        }
    }
    return jsonify(response_object), 200

@app.route('/bills/delete/<int:bill_id>')
def delete_bill(bill_id):
    """Delete a bill"""
    response_object = {
        'status':"Success",
        'bill':"Invalid payload."
    }

    try:
        utils.delete_bill(id=bill_id)
        response_object['bill'] = "bill deleted successfully!"
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["bill"] = "bill has not been deleted!"
        response_object["status"] = "fail"
        return jsonify(response_object),400



if __name__ == "__main__":
    app.run(debug=True, port=3000)