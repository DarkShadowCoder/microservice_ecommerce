import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_checkout_db",
        user="postgres",
        password="postgres"
    )
cur = conn.cursor()


cur.execute("CREATE TABLE orders(id serial PRIMARY KEY NOT NULL,username varchar(150) NOT NULL, status varchar(100) NOT NULL DEFAULT 'pending', date date DEFAULT current_date);")
cur.execute("CREATE TABLE cart(username int NOT NULL, product_name varchar(150),price decimal NOT NULL,status varchar(150) NOT NULL DEFAULT 'Not Checked', date date DEFAULT current_date);")
#cur.execute("CREATE TABLE items(id serial PRIMARY KEY,item_number serial NOT NULL, product_name varchar(150) NOT NULL);")
#cur.execute("ALTER TABLE orders ADD CONSTRAINT fk_cart_id FOREIGN KEY (cart_number) REFERENCES cart(id) ON DELETE CASCADE;")

cur.execute("CREATE TABLE bills(id serial PRIMARY KEY NOT NULL,orders int NOT NULL,date date NOT NULL DEFAULT current_date);")
cur.execute("ALTER TABLE bills ADD CONSTRAINT fk_order_id FOREIGN KEY (orders) REFERENCES orders(id) ON DELETE CASCADE;")

conn.commit()
conn.close()