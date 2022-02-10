from itertools import product
from flask import current_app
from app.models.schemas import RestaurantSchema
from app.models.schemas import MenuSchema
from app.models.schemas import ProductSchema
from app.models.schemas import OrderSchema

from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import get_jwt_identity
from app.models.restaurant import Restaurant
from app.models.menu import Menu
from app.models.product import Product
from app.models.order import Order
from app import db

class RestaurantService:
    @staticmethod
    def get_restaurant(restaurant_id):
        """
        get a restaurant by id"""
        if not (restaurant := Restaurant.query.get(restaurant_id)):
            return err_resp(message="restaurant not found",status=400)
        from .utils import load_restaurant_data
        try:
            restaurant_data = load_restaurant_data(restaurant)
            resp=message(True,"restaurant loaded successfully")
            resp["restaurant"]=restaurant_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant(restaurant_id):
        """
        Delete a restaurant by id"""
        if not (restaurant := Restaurant.query.get(restaurant_id)):
            return err_resp(message="restaurant not found",status=400)
        try:
            db.session.delete(restaurant)
            db.session.commit()
            return message(True,"restaurant deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_restaurant(user_id,restaurant_data):
        """
        Insert a new restaurant"""
        try:
            current_user = get_jwt_identity()
            restaurant = Restaurant(name=restaurant_data["name"],user_id=current_user)
            db.session.add(restaurant)
            db.session.commit()
            return message(True,"restaurant created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_restaurant(restaurant_id,restaurant_data):
        """
        update a restaurant"""
        if not (restaurant:=Restaurant.query.get(restaurant_id)):
            return err_resp(message="restaurant not found",status=400)
        try:
            Restaurant.query.filter_by(id=restaurant_id).update(restaurant_data)
            db.session.commit()
            return message(True,"restaurant updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
    @staticmethod
    def get_restaurants(user_id):
        """
        Get all restaurants of a specific user"""
        if not(restaurants := Restaurant.query.filter_by(user_id=user_id)):
            return err_resp(message="restaurants not found",status=400)
        from .utils import load_restaurant_data
        try:
            restaurants_data = [load_restaurant_data(restaurant) for restaurant in restaurants]
            resp=message(True,"restaurants loaded successfully")
            resp["restaurants"]=restaurants_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    
    @staticmethod
    def get_menu():
        """
        get a menu by id"""
        current_user = get_jwt_identity()
        if not (menu := Menu.query.get(current_user)):
            return err_resp(message="menu not found",status=400)
        from .utils import load_menu_data
        try:
            menu_data = load_menu_data(menu)
            resp=message(True,"menu loaded successfully")
            resp["menu"]=menu_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_menu(menu_data):
        """
        Insert a new menu"""
        try:
            current_user = get_jwt_identity()
            menu = Menu(name=menu_data["name"],restaurant_id=current_user)
            db.session.add(menu)
            db.session.commit()
            return message(True,"menu created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_menu(menu_id,menu_data):
        """
        update a menu"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(message="menu not found",status=400)
        try:
            Menu.query.filter_by(id=menu_id).update(menu_data)
            db.session.commit()
            return message(True,"menu updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_products(menu_id):
        """
        Get all products of a specific menu"""
        if not(products := Product.query.filter_by(menu_id=menu_id)):
            return err_resp(message="restaurants not found",status=400)
        from .utils import load_product_data
        try:
            products_data = [load_product_data(product) for product in products]
            resp=message(True,"restaurants loaded successfully")
            resp["products"]=products_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_product(product_id):
        """
        get a product by id"""
        if not (product := Product.query.get(product_id)):
            return err_resp(message="product not found",status=400)
        from .utils import load_product_data
        try:
            product_data = load_product_data(product)
            resp=message(True,"product loaded successfully")
            resp["product"]=product_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_product(product_data, menu_id):
        """
        Insert a new product"""
        try:
            product = Product(name=product_data["name"],detailed_info=product_data["detailed_info"],price=product_data["price"],image_url=product_data["image_url"],menu_id=menu_id)
            db.session.add(product)
            db.session.commit()
            return message(True,"product created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_product(product_id,product_data):
        """
        Update a product"""
        if not (product:=Product.query.get(product_id)):
            return err_resp(message="product not found",status=400)
        try:
            Product.query.filter_by(id=product_id).update(product_data)
            db.session.commit()
            return message(True,"product updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_product(product_id):
        """
        Delete a product by id"""
        if not (product := Product.query.get(product_id)):
            return err_resp(message="product not found",status=400)
        try:
            db.session.delete(product)
            db.session.commit()
            return message(True,"product deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()