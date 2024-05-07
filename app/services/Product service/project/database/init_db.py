import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_products_db",
        user="postgres",
        password="postgres",
    )
cur = conn.cursor()

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_products_db",
        user="postgres",
        password="postgres",
    )
    return conn

def set_product(name, category, price, description, image_path):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name,category,price,description,image_path) VALUES(%s,%s, %s, %s,%s);",(name,category,price,description,image_path))
    conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS category(name varchar(200) PRIMARY KEY);")
cur.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(200) NOT NULL, category varchar(200) NOT NULL, price decimal NOT NULL, description text, date time without time zone DEFAULT current_time, image_path varchar(300)) ;")
#cur.execute("ALTER TABLE  products ADD CONSTRAINT fk_category_name FOREIGN KEY (category) REFERENCES category(name) ON DELETE CASCADE;")
set_product()



conn.commit()
conn.close()