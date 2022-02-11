from flask import current_app
from app.models.schemas import OrderSchema, OrderDetailSchema

from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import get_jwt_identity
from app.models.order import Order
from app.models.order_detail import OrderDetail
from constants.texts import Texts

from app import db

class CustomerService:
    @staticmethod
    def get_orders():
        """
        get all orders"""
        current_user = get_jwt_identity()
        if not (orders := Order.query.filter_by(user_id=current_user)):
            return err_resp(message=Texts.ORDER_NOT_FOUND_ERR,status=400)
        from .utils import load_order_data
        try:
            order_data = [load_order_data(order) for order in orders]
            resp=message(True,Texts.ORDERS_SUCCESS)
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_order(order_id):
        """
        Delete a order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(message=Texts.ORDER_NOT_FOUND_ERR,status=400)
        try:
            # Deleted with order detail
            db.session.delete(order)
            db.session.commit()
            return message(True,Texts.ORDER_DELETE_SUCCESS)
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_order(restaurant_id,order_data):
        """
        Insert a new order"""
        try:
            current_user = get_jwt_identity()
            # Firstly create an order
            order = Order(no=order_data['no'],status=order_data['status'],user_id=current_user,restaurant_id=restaurant_id)
            # Then add order detail with order id
            order_item = OrderDetail(product_id=order_data['items']['product_id'], quantity=order_data['items']['quantity'], order_id=order.id)
            db.session.add(order_item)

            order.items.append(order_item)
    
            db.session.add(order)
            db.session.commit()

            return message(True,Texts.ORDER_CREATE_SUCCESS)
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    
    @staticmethod
    def get_order(order_id):
        """
        Get an order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(message=Texts.ORDER_NOT_FOUND_ERR,status=400)
        from .utils import load_order_data, load_order_detail_data
        try:
            order_detail = order.items
            detail = [load_order_detail_data(item) for item in order_detail]
            order_data = load_order_data(order)
            # Added items in order
            order_data['items'] = detail
            resp=message(True,Texts.ORDERS_SUCCESS)
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order(order_id,order_data):
        """
        update an order"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(message=Texts.ORDER_NOT_FOUND_ERR,status=400)
        try:
            Order.query.filter_by(id=order_id).update(order_data)
            db.session.commit()
            return message(True,Texts.ORDER_UPDATE_SUCCESS)
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()