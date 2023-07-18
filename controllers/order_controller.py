from flask import Blueprint, render_template
from models.order_list import order_list

orders_blueprint = Blueprint("order_list", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title = "My Orders", order_list=order_list , single_order = order_list)


