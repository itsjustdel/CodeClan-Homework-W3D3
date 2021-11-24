from flask import render_template
from app import app
from models.order import orders

@app.route("/orders")
def list():
    return render_template("index.html", title="Mr Pepper's Wreck 'Em Ranch", orders=orders)

@app.route("/orders/<index>")
def show_order(index):
    # get order to send to page, we need to cast the passed string to an int to access list
    intIndex = int(index)
    order = orders[intIndex]
    return render_template("order.html", title="Mr Pepper's Wreck 'Em Ranch", order=order, index=intIndex)

