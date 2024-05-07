import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_inventory_db",
        user="postgres",
        password="postgres",
    )
cur = conn.cursor()


#cur.execute("CREATE TABLE IF NOT EXISTS Invoice(users,);")
cur.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(200) NOT NULL, category varchar(200) NOT NULL, price decimal NOT NULL, description text, date time without time zone DEFAULT current_time, image_path varchar(300)) ;")
#cur.execute("ALTER TABLE  products ADD CONSTRAINT fk_category_name FOREIGN KEY (category) REFERENCES category(name) ON DELETE CASCADE;")


conn.commit()
conn.close()