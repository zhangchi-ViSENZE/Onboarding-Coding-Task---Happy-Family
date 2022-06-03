from database import *

conn = create_connection('database.db')
print(select_all_products(conn))
terminate_connection(conn)