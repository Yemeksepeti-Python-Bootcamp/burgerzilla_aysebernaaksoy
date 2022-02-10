from flask import current_app
from app.models.schemas import OrderSchema, OrderDetailSchema

from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import get_jwt_identity
from app.models.order import Order
from app.models.order_detail import OrderDetail

from app.models.menu import Menu
from app import db

class CustomerService:
    @staticmethod
    def get_orders():
        """
        get all orders"""
        current_user = get_jwt_identity()
        if not (orders := Order.query.filter_by(user_id=current_user)):
            return err_resp(message="order not found",status=400)
        from .utils import load_order_data
        try:
            order_data = [load_order_data(order) for order in orders]
            resp=message(True,"orders loaded successfully")
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
            return err_resp(message="order not found",status=400)
        try:
            # Deleted with order detail
            db.session.delete(order)
            db.session.commit()
            return message(True,"restaurant deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_order(restaurant_id,order_data):
        """
        Insert a new restaurant"""
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

            return message(True,"restaurant created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    # @staticmethod
    # def update_restaurant(restaurant_id,restaurant_data):
    #     """
    #     update a restaurant"""
    #     if not (restaurant:=Restaurant.query.get(restaurant_id)):
    #         return err_resp(message="restaurant not found",status=400)
    #     try:
    #         Restaurant.query.filter_by(id=restaurant_id).update(restaurant_data)
    #         db.session.commit()
    #         return message(True,"restaurant updated successfully")
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()
        
    # @staticmethod
    # def get_restaurants(user_id):
    #     """
    #     Get all restaurants of a specific user"""
    #     if not(restaurants := Restaurant.query.filter_by(user_id=user_id)):
    #         return err_resp(message="restaurants not found",status=400)
    #     from .utils import load_restaurant_data
    #     try:
    #         restaurants_data = [load_restaurant_data(restaurant) for restaurant in restaurants]
    #         resp=message(True,"restaurants loaded successfully")
    #         resp["restaurants"]=restaurants_data
    #         return resp,200
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()
    
    @staticmethod
    def get_order(order_id):
        """
        get an order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(message="order not found",status=400)
        from .utils import load_order_data, load_order_detail_data
        try:
            order_detail = order.items
            detail = load_order_detail_data(order_detail[0])
            order_data = load_order_data(order)
            # Added items in order
            order_data['items'] = detail
            resp=message(True,"order loaded successfully")
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    # @staticmethod
    # def insert_menu(restaurant_id,menu_data):
    #     """
    #     Insert a new menu"""
    #     try:
    #         menu = Menu(name=menu_data["name"],detailed_info=menu_data["detailed_info"],price=menu_data["price"],image_url=menu_data["image_url"],restaurant_id=restaurant_id)
    #         db.session.add(menu)
    #         db.session.commit()
    #         return message(True,"menu created successfully")
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()
