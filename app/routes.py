from flask import jsonify, request, Blueprint

from app.models import Order, Session

from .controllers import delete_order_by_id, get_all_orders,create_new_order, get_user_orders, update_order_by_id, get_order_by_id

order_routes = Blueprint("orders", __name__)

@order_routes.route('/',methods=['GET'])
def get_orders():
    try:
        orders = get_all_orders()
        return jsonify({"orders": orders}), 200
    except Exception as e:
        return jsonify({"message": "Failed to fetch orders", "error": str(e)}), 400


@order_routes.route('/create',methods=['POST'])
def create_order():
    order_data = request.get_json()
    try:
        create_new_order(order_data)
        return jsonify({"message": "Order Created successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@order_routes.route('/user/<int:user_id>',methods=['GET'])
def get_user_orders_by_id(user_id):
    try:
        user_orders = get_user_orders(user_id)
        return jsonify({"user_orders": user_orders}), 200

    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@order_routes.route('/<order_id>', methods=['GET'])
def get_order_detailes(order_id):
    order = get_order_by_id(order_id)
    if order:
        return jsonify({"order": order})
    return jsonify({"message": "Order not found"}), 404


@order_routes.route('/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        delete_result = delete_order_by_id(order_id)
        if delete_result:
            return jsonify({"message": "Order deleted successfully"}), 200
        else:
            return jsonify({"message": "Order not found"}), 404
    except Exception as e:
        return jsonify({"message": "Failed to delete order", "error": str(e)}), 400

@order_routes.route('/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order_data = request.get_json()
        executed = order_data.get('executed')
        # Assuming the 'executed' field is included in the request JSON

        update_result = update_order_by_id(order_id, executed)
        if update_result:
            return jsonify({"message": "Order updated successfully"}), 200
        else:
            return jsonify({"message": "Order not found"}), 404
    except Exception as e:
        return jsonify({"message": "Failed to update order", "error": str(e)}), 400




