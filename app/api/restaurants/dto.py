from flask_restx import Namespace,fields

class RestaurantDto:
    api = Namespace('restaurants', description='restaurants related operations')
    restaurant = api.model('restaurant', {
        'id':fields.Integer,
        'name':fields.String,
        'user_id':fields.Integer,
    })

    restaurant_resp = api.model('restaurant_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurant':fields.Nested(restaurant)
    })

    restaurant_list_resp = api.model('restaurant_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurants':fields.List(fields.Nested(restaurant))})

    menu_api = Namespace('menu', description='menus related operations')
    menu = menu_api.model('menu', {
        'id':fields.Integer,
        'name':fields.String,
        'restaurant_id':fields.Integer,
    })

    prodcut_api = Namespace('products', description='products related operations')
    product = api.model('product', {
        'id':fields.Integer,
        'name':fields.String,
        'detailed_info':fields.String,
        'price':fields.String,
        'image_url':fields.String,
        'menu_if':fields.Integer
    })
    product_resp = api.model('product_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'product':fields.Nested(product)
    })

    order = api.model('order', {
        'id':fields.Integer,
        'no':fields.String,
        'status':fields.String,
        'items':fields.String
    })

    order_resp = api.model('order_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'orders':fields.List(fields.Nested(order))})