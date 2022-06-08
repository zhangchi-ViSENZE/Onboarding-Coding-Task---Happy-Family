import sqlite3
from sqlite3 import Error

# establish connection with database file


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Connect successfully with ', db_file,
              ' using sqlite ', sqlite3.version)
        return conn
    except Error as e:
        print(e)
        exit(0)

# terminate connection with database file


def terminate_connection(conn):
    if conn:
        conn.close()
        print('Connection terminated successfully!')
    else:
        print('Connection terminated unsuccessfully!')

# create table in database


def create_table(conn, create_table_sql):
    try:
        conn.cursor().execute(create_table_sql)
        print('Table created successfully!')
    except Error as e:
        print('Table created unsuccessfully!')
        print(e)
        exit(0)

# insert product data into database


def create_product(conn, product):
    create_product_sql = ''' INSERT INTO products(product_name,quantity) 
                             VALUES(?,?) '''
    try:
        conn.cursor().execute(create_product_sql, product)
        conn.commit()
        print('Product inserted successfully!')
    except Error as e:
        print('Product inserted unsuccessfully!')
        print(e)
        exit(0)

# update product data


def update_product(conn, product_for_sql):
    try:
        conn.cursor().execute(''' UPDATE products
                             SET quantity = ?
                             WHERE product_name = ? ''', product_for_sql)
        conn.commit()
        print('Product updated successfully!')
    except Error as e:
        print('Product updated unsuccessfully!')
        print(e)
        exit(0)

# query all rows from products


def select_all_products(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")

    return cur.fetchall()

# quey product data


def select_product_by_product_name(conn, product_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE product_name = '" +
                product_name + "'")
    return cur.fetchall()


# initialise the database
if __name__ == '__main__':
    database = "database.db"

    # create database connection
    conn = create_connection(database)

    # create products table
    create_table_sql = """ CREATE TABLE IF NOT EXISTS products (
                                        product_name varchar(50) PRIMARY KEY,
                                        quantity int DEFAULT 1
                                    ); """
    create_table(conn, create_table_sql)

    # insert data into database
    product1 = ('milk', 100)
    product2 = ('eggs', 30)

    create_product(conn, product1)
    create_product(conn, product2)

    # terminate connection
    terminate_connection(conn)
