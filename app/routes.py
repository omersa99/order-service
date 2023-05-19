from flask import jsonify, request, Blueprint

from .controllers import get_all_orders,create_new_order, get_user_orders

order_routes = Blueprint("orders", __name__)

@order_routes.route('/',methods=['GET'])
def index():
    try:
        orders = get_all_orders()
        return jsonify(orders), 200
    except:
        return jsonify({"message"}), 400

@order_routes.route('/create',methods=['POST'])
def create_order():
    order_data = request.get_json()
    try:
        create_new_order(order_data)
        return jsonify({"message": "Order Created successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@order_routes.route('/<int:user_id>',methods=['GET'])
def get_user_orders_by_id(user_id):
    try:
        user_orders = get_user_orders(user_id)
        if user_orders:
            return jsonify(user_orders), 200
        else:
            return jsonify({"message": "no such user "}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

