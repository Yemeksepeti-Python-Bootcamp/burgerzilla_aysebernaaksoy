from flask import current_app
from app.api.customers.controller import Order
from app.models.schemas import OrderSchema

from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import get_jwt_identity
from app.models.order import Order
from app.models.menu import Menu
from app import db

class CustomerService:
    @staticmethod
    def get_order(customer_id):
        """
        get a order by id"""
        if not (order := Order.query.get(customer_id)):
            return err_resp(message="order not found",status=400)
        from .utils import load_order_data
        try:
            order_data = load_order_data(order)
            resp=message(True,"orders loaded successfully")
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    # @staticmethod
    # def delete_restaurant(restaurant_id):
    #     """
    #     Delete a restaurant by id"""
    #     if not (restaurant := Restaurant.query.get(restaurant_id)):
    #         return err_resp(message="restaurant not found",status=400)
    #     try:
    #         db.session.delete(restaurant)
    #         db.session.commit()
    #         return message(True,"restaurant deleted successfully")
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()

    # @staticmethod
    # def insert_restaurant(user_id,restaurant_data):
    #     """
    #     Insert a new restaurant"""
    #     try:
    #         current_user = get_jwt_identity()
    #         restaurant = Restaurant(name=restaurant_data["name"],user_id=current_user)
    #         db.session.add(restaurant)
    #         db.session.commit()
    #         return message(True,"restaurant created successfully")
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()

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
    
    # @staticmethod
    # def get_menu(restaurant_id):
    #     """
    #     get a menu by id"""
    #     if not (menu := Menu.query.filter_by(restaurant_id=restaurant_id)):
    #         return err_resp(message="menu not found",status=400)
    #     from .utils import load_menu_data
    #     try:
    #         menu_data = load_menu_data(menu)
    #         resp=message(True,"menu loaded successfully")
    #         resp["menu"]=menu_data
    #         return resp,200
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()

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
