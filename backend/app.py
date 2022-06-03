from database import *
from flask import Flask, jsonify, make_response, render_template, request, send_file

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# query store for product availability
@app.route("/store/<has_product>", methods = ['GET'])
def query_product(has_product):
    # process the url
    product_name = has_product[3:]
    
    # set up database connection
    conn = create_connection('database.db')

    quantity = select_product_by_product_name(conn,product_name)
    # terminate database connection
    terminate_connection(conn)

    if quantity:
        resp = jsonify(quantity)
        resp.status_code = 200
        return resp
    else:
        print('Product name incorrect!')
        return 'Not found', 404

# buy product from store
@app.route("/store/<buy_product>", methods = ['POST'])
def buy_product(buy_product):
    # process the url
    product_name = buy_product[3:]
    
    # set up database connection
    conn = create_connection('database.db')

    product = select_product_by_product_name(conn,product_name)

    if not product:
        print('Product name incorrect!')
        return {
                "error_code": 404,
                "error_msg": 'Product not found and Unsuccessful Purchase'
                },404
    
    product = product[0]
    quantity = product[2]
    req_quantity = int(request.args['quantity'])

    if req_quantity <= 0:
        print('Product quantity invalid! Should be a positive integer.')
        return {
                "error_code": 101,
                "error_msg": 'Parameter must be a positive integer.'
                },400

    if quantity < req_quantity:
        print('Product quantity invalid! Should be smaller than the avaliability.')
        return {
                "error_code": 400,
                "error_msg": 'Parameter must be smaller than the current avaliability.'
                },400

    update_product(conn,(product[1],quantity-req_quantity,product[3],product[0]))

    # terminate database connection
    terminate_connection(conn)

    return "Successful Purchase",200
        

if __name__ == '__main__':
    app.debug=True
    app.run()
    
#     conn = create_connection('database.db')
#     select_all_products(conn)
#     select_product_by_product_name(conn,'milk')
#     terminate_connection(conn)
