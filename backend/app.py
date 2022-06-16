from database import *
from flask import Flask
from flask import abort
from flask import jsonify
from flask import render_template
from flask import request
from flask import json
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")

# query store for product availability


@app.route("/store/<has_product>", methods=['GET'])
def query_product(has_product):
    # process the url
    product_name = has_product

    # set up database connection
    conn = create_connection('database.db')

    product = select_product_by_product_name(conn, product_name)

    # terminate database connection
    terminate_connection(conn)

    if product:
        quantity = product[0][1]
        response = jsonify({"name": product_name, "quantity": quantity})
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    else:
        print('Product name incorrect!')
        abort(404, {"error_msg": 'Product not found'})

# buy product from store


@app.route("/store/<buy_product>", methods=['POST'])
def buy_product(buy_product):
    # process the url
    product_name = buy_product

    # set up database connection
    conn = create_connection('database.db')

    product = select_product_by_product_name(conn, product_name)

    if not product:
        print('Product name incorrect!')
        return abort(404, {
            "error_msg": 'Product not found and Unsuccessful Purchase'
        })

    product_name = product[0][0]
    quantity = product[0][1]
    req_quantity = int(request.args.get('quantity'))

    if req_quantity <= 0:
        print('Product quantity invalid! Should be a positive integer.')
        abort(400, {
            "error_msg": 'Parameter must be a positive integer.'
        })

    if quantity < req_quantity:
        print('Product quantity invalid! Should be smaller than the avaliability.')
        return abort(400, {
            "error_msg": 'Parameter must be smaller than the current avaliability.'
        })

    update_product(conn, (quantity-req_quantity, product_name))

    # terminate database connection
    terminate_connection(conn)

    response = jsonify({"name": product_name, "quantity": req_quantity})
    response.status_code = 200
    response.headers['Access-Control-Allow-Origin'] = '*'
    print(response)
    return response


@app.errorhandler(HTTPException)
def handle_exception(e):
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "error_code": e.code,
        "error_msg": e.description["error_msg"],
    })
    response.content_type = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
