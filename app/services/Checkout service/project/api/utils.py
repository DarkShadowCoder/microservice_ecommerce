import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_checkout_db",
        order="postgres",
        password="postgres"
    )
    return conn

### ORDERS TABLE OPERATIONS

def get_all_orders():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM orders;")
    return cur.fetchall()

def get_order_by_user(username):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM orders WHERE username='"+str(username)+"';")
    return cur.fetchall()

def get_order_by_cart(username):
    cur = get_db_connection().cursor()
    cur.execute("SELECT o.id, o.username, o.status, o.date, c.product_name,c.price FROM orders AS o JOIN cart AS c ON (o.username = c.username) WHERE username=%s;",username)
    return cur.fetchall()

def get_order(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM orders WHERE id="+str(id)+";")
    return cur.fetchone()


def set_order(username, status='pending'):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders(username,status) VALUES(%s, %s);",(username,status))
    conn.commit()

def delete_order(order_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM orders WHERE id=%s",order_id)
    conn.commit()

def order_json(liste:tuple):
    json = {}
    json['username'] = liste[1]
    json['date'] = liste[3]
    json['status'] = liste[2]
    return json

############     CART TABLE OPERATION    ############

def get_all_carts():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM carts;")
    return cur.fetchall()

def get_cart_by_user(username):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM carts WHERE username='"+str(username)+"';")
    return cur.fetchall()

def get_carts_by_product(product_name):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM orders WHERE product_name='%s';",product_name)
    return cur.fetchall()

def get_carts_by_item(item:int):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM orders WHERE item='%s';",item)
    return cur.fetchall()

def get_cart(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM carts WHERE id="+str(id)+";")
    return cur.fetchone()

def set_cart(number,product_name, status='pending'):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO carts(username,cart_number,status) VALUES(%s,%s, %s);",(username,cart_number,status))
    conn.commit()

def delete_cart(order_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM carts WHERE id=%s",order_id)
    conn.commit()

def cart_json(liste:tuple):
    json = {}
    json['number'] = liste[1]
    json['product'] = liste[3]
    json['user_id'] = liste[2]
    json['item'] = liste[4]
    json["price"] = liste[5]
    json['date'] = liste[6]
    return json


############     BILL TABLE OPERATION    ############


def get_all_bills():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM bills;")
    return cur.fetchall()

def get_bill_by_orders(orders):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM bills WHERE username=%s;",orders)
    return cur.fetchone()

def get_bill(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM bills WHERE id=%s;",id)
    return cur.fetchone()


def set_bill(orders):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO bills(orders) VALUES(%s);",orders)
    conn.commit()

def delete_bill(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM bills WHERE id=%s",id)
    conn.commit()

def bill_json(liste:tuple):
    json = {}
    json['order_id'] = liste[1]
    return json