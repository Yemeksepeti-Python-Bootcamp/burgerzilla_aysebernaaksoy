from app import ma
from .user import User
from .restaurant import Restaurant
from .menu import Menu

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date", "role_id")

class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "user_id")    

class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class ProductSchema(ma.Schema):
     class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "detailed_info", "price", "image_url", "menu_id")

class OrderSchema(ma.Schema):
     class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "no", "status", "restaurant_id")

class OrderDetailSchema(ma.Schema):
     class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "quantity", "order_id", "product_id")