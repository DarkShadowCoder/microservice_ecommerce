import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_products_db",
        user="postgres",
        password="postgres",
    )
    return conn

def get_all_products():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM products;")
    return cur.fetchall()

def get_product_by_name(name):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM products WHERE name='"+str(name)+"';")
    return cur.fetchone()

def get_product(id):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM products WHERE id="+str(id)+";")
    return cur.fetchone()


def set_product(name, category, price, description, image_path):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name,category,price,description,image_path) VALUES(%s,%s, %s, %s,%s);",(name,category,price,description,image_path))
    conn.commit()


def delete_product(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=%s",id)
    conn.commit()


#### Category operation

def get_all_categories():
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM category;")
    return cur.fetchall()

def get_category(name):
    cur = get_db_connection().cursor()
    cur.execute("SELECT * FROM category WHERE name='"+str(name)+"';")
    return cur.fetchone()


def set_category(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO category(name) VALUES(%s);",(name))
    conn.commit()


def delete_category(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM category WHERE name=%s",name)
    conn.commit()

#### Formating data

def product_json(liste:tuple):
    json = {}
    json['name'] = liste[1]
    json['category'] = liste[2]
    json['price'] = liste[3]
    json['description'] = liste[4]
    json['image_path'] = liste[5]
    return json

def category_json(liste:tuple):
    json = {}
    json["name"] = liste[0]
    
