import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_users_db",
        user="postgres",
        password="postgres",
    )
    return conn

### USERS TABLE OPERATIONS

def get_all_user():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM users;")
    return cur.fetchall()

def get_user_by_email(email):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM users WHERE email='"+str(email)+"';")
    return cur.fetchone()

def get_user(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM users WHERE id="+str(id)+";")
    return cur.fetchone()

def get_user_by_client():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM users WHERE isadmin='true';")

    return cur.fetchall()

def set_user(username, email, password,isadmin='false'):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users(username,email,password,isadmin) VALUES(%s,%s, %s, %s);",(username,email,password,isadmin))
    conn.commit()

def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s",user_id)
    conn.commit()

def user_json(liste:tuple):
    json = {}
    json['username'] = liste[1]
    json['email'] = liste[2]
    json['date'] = liste[5]
    json['isadmin'] = liste[4]
    return json

### REVIEWS TABLE OPERATION
def get_all_reviews():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM reviews;")
    return cur.fetchall()

def get_review_by_user(user_id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM users WHERE user_id="+str(user_id)+";")
    return cur.fetchall()

def get_review(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM reviews WHERE id="+str(id)+";")
    return cur.fetchone()

def set_review(user_id, product_id, rating, review):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO reviews(user_id,product_id,rating,review) VALUES(%s,%s, %s, %s);",(user_id,product_id,rating,review))
    conn.commit()

def delete_review(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM reviews WHERE id="+str(id)+";")
    conn.commit()

def review_json(liste:tuple):
    json = {}
    json['user_id'] = liste[1]
    json['product_id'] = liste[2]
    json['rating'] = liste[3]
    json['review'] = liste[4]
    json['date'] = liste[5]
    return json

#### MESSAGE TABLE OPERATION
def get_all_messages():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM messages;")
    return cur.fetchall()

def get_message_by_user(user_id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM messages WHERE email='"+str(user_id)+"';")
    return cur.fetchall()

def get_message(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM messages WHERE id="+str(id)+";")
    return cur.fetchone()



def set_message(user_id, message):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages(user_id,message) VALUES(%s,%s);",(user_id,message))
    conn.commit()

def delete_message(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE id="+str(id)+";")
    conn.commit()

def message_json(liste:tuple):
    json = {}
    json['user_id'] = liste[1]
    json['message'] = liste[2]
    json['date'] = liste[3]
    return json
