from flask_restx import Namespace,fields

class OrderDto:
    api = Namespace('orders', description='orders related operations')
    order = api.model('order', {
        'id':fields.Integer,
        'no':fields.String,
        'restaurant_id':fields.Integer,
        'user_id':fields.Integer,
        'menu_id':fields.Integer,
        'status':fields.String
    })

    order_resp = api.model('order_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'order':fields.Nested(order)
    })

    order_list_resp = api.model('order_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'orders':fields.List(fields.Nested(order))})

    # menu_api = Namespace('menus', description='menus related operations')
    # menu = menu_api.model('menu', {
    #     'id':fields.Integer,
    #     'name':fields.String,
    #     'detailed_info':fields.String,
    #     'price':fields.String,
    #     'image_url':fields.String,
    #     'restaurant_id':fields.Integer,
    # })

    # restaurant_resp = api.model('restaurant_resp', {
    #     'status':fields.Boolean,
    #     'message':fields.String,
    #     'restaurant':fields.Nested(restaurant)
    # })

    # restaurant_list_resp = api.model('restaurant_list_resp', {
    #     'status':fields.Boolean,
    #     'message':fields.String,
    #     'restaurants':fields.List(fields.Nested(restaurant))})