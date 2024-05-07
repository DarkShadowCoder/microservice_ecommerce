import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_users_db",
        user="postgres",
        password="postgres",
    )
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,username varchar(50) UNIQUE NOT NULL, email varchar(100) UNIQUE NOT NULL, password varchar(150) NOT NULL, isadmin boolean NOT NULL DEFAULT false , date date DEFAULT current_date)")
cur.execute("CREATE TABLE IF NOT EXISTS reviews(id serial PRIMARY KEY, user_id int NOT NULL, product_id int NOT NULL,rating int NOT NULL DEFAULT 1, review TEXT, date date DEFAULT current_date)")
cur.execute("CREATE TABLE IF NOT EXISTS messages(id serial, user_id int NOT NULL, message TEXT, date date DEFAULT current_date)")

cur.execute("ALTER TABLE messages ADD CONSTRAINT fk_message_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;")
cur.execute("ALTER TABLE reviews ADD CONSTRAINT fk_reviews_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;")

#cur.execute("INSERT INTO users(username,email,password,isadmin) VALUES ('yvan','yvanlandry@gmail.com','yvan1234',true),('diva','divapams@gmail.com','diva1234',true),('junior','evelynjunior@gmail.com','junior1234',false)")
conn.commit()
conn.close()