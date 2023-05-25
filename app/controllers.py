from flask import jsonify
from .models import Session, Order



def get_all_orders():
    session = Session()
    orders = session.query(Order).all()
    # print(orders)
    data = []
    for order in orders:
        data.append({
            "order_id":order.id,
            "user_id":order.user_id,
            "stock id":order.stock_id,
            "status":order.executed,
            "created at":order.created_at
        })
    return data

def create_new_order(order_data):
    try:
        user_id = order_data.get('user_id')
        stock_id = order_data.get('stock_id')
        type = order_data.get('type')
        price = order_data.get('price')
        shares = order_data.get('shares')

        # Validation Requared
        if not user_id or not stock_id or not type or not price or not shares:
            raise ValueError("Invalid Stock data. Please provide all required fields.")


        new_order = Order(user_id=user_id,stock_id=stock_id,type=type,price=price,shares=shares)

        session = Session()
        session.add(new_order)
        session.commit()
        return new_order.id
    except Exception as e:
        raise e

def get_user_orders(user_id):
    session = Session()

    if not user_id:
        raise ValueError("Invalid user id.")

    orders = session.query(Order).filter(Order.user_id == user_id).all()
    data = []
    for order in orders:
        data.append({
            "user_id":order.user_id,
            "stock id":order.stock_id,
            "status":order.executed,
            "created at":order.created_at
        })
    return data

def delete_order_by_id(order_id):
    try:
        session = Session()
        order = session.query(Order).get(order_id)

        if order:
            session.delete(order)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        raise e

def update_order_by_id(order_id, executed):
    try:
        session = Session()
        order = session.query(Order).get(order_id)
        if order:
            order.executed = executed
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        raise e
