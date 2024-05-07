from flask import flash, Flask, render_template, request, jsonify,session
import utils
from sqlalchemy import exc


app = Flask(__name__)

conn = utils.get_db_connection()
cur = conn.cursor()

@app.route('/users', methods=["POST"])
def add_user():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')

    try:
        user = utils.get_user_by_email(email)
        if not user:
            utils.set_user(username,email,password)
            user = utils.get_user_by_email(email)
            response_object['status'] = 'success'
            response_object['message'] = f'{username} was created'
            return jsonify(response_object),201
        
        else:
            response_object["message"] = "Sorry. That username or email already exists"
            return jsonify(response_object),400
    except exc.IntegrityError as e:
        session.clear()
        return jsonify(response_object),400

@app.route('/users/<int:user_id>', methods=["GET"])
def get_single_users(user_id):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message':'User does not exist'
    }
    try:
        user = utils.get_user(user_id)
        if not user:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':user[0],
                    'username':user[1],
                    'email':user[2],
                    'date': user[3]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/users',methods={'GET'})
def get_all_users():
    """Get all users"""
    response_object = {
        'status':'success',
        'data':{
            'users':[utils.user_json(user) for user in utils.get_all_user()]
        }
    }
    return jsonify(response_object), 200

@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):
    """Delete a user"""
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    else:
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')
        try:
            utils.delete_user()
            response_object['message'] = "User deleted successfully!"
            return jsonify(response_object),201
        except exc.IntegrityError as e:
            response_object["message"] = "User has not been deleted!"
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
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    user_id = post_data.get('user_id')
    rating = post_data.get('rating')
    product_id = post_data.get('product_id')
    review = post_data.get('review')

    try:
        utils.set_review(user_id,product_id,rating, review)
        response_object['status'] = 'success'
        response_object['message'] = f'review was created'
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["message"] = "Order post failled"
        session.clear()
        return jsonify(response_object),400

@app.route('/reviews/<int:review_id>', methods=["GET"])
def get_single_review(review_id):
    """Get single review details"""
    response_object = {
        'status': 'fail',
        'message':'Review does not exist'
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
                    'user_id':review[1],
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
        'message':"Invalid payload."
    }

    try:
        utils.delete_review(id=review_id)
        response_object['message'] = "review deleted successfully!"
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["message"] = "review has not been deleted!"
        response_object["status"] = "fail"
        return jsonify(response_object),400


####################################################################
# ##############        MESSAGES ROUTES      ########################
####################################################################


@app.route('/messages', methods=["POST"])
def add_message():
    post_data = request.get_json() 
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    if not post_data:
        return jsonify(response_object),400
    user_id = post_data.get('user_id')
    message = post_data.get('message')

    try:
        utils.set_message(user_id,message)
        response_object['status'] = 'success'
        response_object['message'] = f'Message was created'
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["message"] = "Message post failled"
        session.clear()
        return jsonify(response_object),400

@app.route('/messages/<int:message_id>', methods=["GET"])
def get_single_message(message_id):
    """Get single message details"""
    response_object = {
        'status': 'fail',
        'message':'Message does not exist'
    }
    try:
        message = utils.get_message(message_id)
        if not message:
            return jsonify(response_object),404
        else:
            response_object = {
                'status':'success',
                'data':{
                    'id':message[0],
                    'user_id':message[1],
                    'message':message[2],
                    'date': message[3]
                }
            }
            return jsonify(response_object),200
    except ValueError:
        return jsonify(response_object),404

@app.route('/messages',methods=['GET'])
def get_all_messages():
    """Get all messages"""
    response_object = {
        'status':'success',
        'data':{
            'messages':[utils.message_json(message) for message in utils.get_all_messages()]
        }
    }
    return jsonify(response_object), 200

@app.route('/messages/delete/<int:message_id>')
def delete_message(message_id):
    """Delete a message"""
    response_object = {
        'status':"Success",
        'message':"Invalid payload."
    }

    try:
        utils.delete_message(id=message_id)
        response_object['message'] = "message deleted successfully!"
        return jsonify(response_object),201
    except exc.IntegrityError as e:
        response_object["message"] = "message has not been deleted!"
        response_object["status"] = "fail"
        return jsonify(response_object),400



if __name__ == "__main__":
    app.run(debug=True, port=3000)