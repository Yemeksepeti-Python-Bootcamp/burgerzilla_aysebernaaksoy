from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import CustomerService
from .dto import OrderDto

api = OrderDto.api
order=OrderDto.order
order_resp=OrderDto.order_resp
order_list_resp=OrderDto.order_list_resp

@api.route('/<int:restaurant_id>')
class Order(Resource):
    @api.doc('get specific restaurant',responses={
        200:('Success',order_resp),
        400:'Invalid restaurant ID',
    })
    @jwt_required()
    def get(self,customer_id):
        """ get specific restaurant"""
        return CustomerService.get_restaurant(customer_id)
    
#     @api.doc("Delete a specific customer",responses={
#         200:"Success"})
#     @jwt_required()
#     def delete(self,restaurant_id):
#         """ Delete a specific restaurant"""
#         return RestaurantService.delete_restaurant(restaurant_id)

#     @api.doc("Update a specific restaurant",responses={200:"Success"})
#     @api.expect(restaurant)
#     @jwt_required()
#     def put(self,restaurant_id):
#         """ Update a specific restaurant"""
#         data = request.get_json()
#         return RestaurantService.update_restaurant(restaurant_id,data)

# @api.route("/user/<int:user_id>")
# class RestaurantList(Resource):
#     @api.doc("Get all restaurant of a specific user",responses={200:"Success",500:"Internal Server Error"})
#     @jwt_required()
#     def get(self,user_id):
#         """
#         Get all restaurant of a specific user"""
#         return RestaurantService.get_restaurants(user_id)


#     @api.doc("Create a new restaurant",responses={200:"Success",500:"Internal Server Error"})
#     @api.expect(restaurant)
#     @jwt_required()
#     def post(self,user_id):
#         """
#         Create a new restaurant"""
#         data = request.get_json()
#         return RestaurantService.insert_restaurant(user_id,data)

# @api.route("/menu/<int:restaurant_id>")
# # TODO:Giren kullanıcının id si restaurant id si ise o zaman işlemler yapılsın
# class MenuList(Resource):
#     @api.doc("Get all menu of a specific restaurant",responses={200:"Success",500:"Internal Server Error"})
#     @jwt_required()
#     def get(self,restaurant_id):
#         """
#         Get all menu of a specific restaurant"""
#         return RestaurantService.get_menu(restaurant_id)

#     @api.doc("Create a new menu",responses={200:"Success",500:"Internal Server Error"})
#     @api.expect(restaurant)
#     @jwt_required()
#     def post(self,restaurant_id):
#         """
#         Create a new restaurant"""
#         data = request.get_json()
#         return RestaurantService.insert_menu(restaurant_id,data)