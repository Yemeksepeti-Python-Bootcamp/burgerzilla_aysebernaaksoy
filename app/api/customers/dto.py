from flask_restx import Namespace,fields

class CustomerDto:
    api = Namespace('customers', description='orders related operations')
    customer = api.model('customer', {
        'id':fields.Integer,
        'no':fields.String,
        'restaurant_id':fields.Integer,
        'user_id':fields.Integer,
        'menu_id':fields.Integer,
        'status':fields.String
    })

    customer_resp = api.model('customer_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'customer':fields.Nested(customer)
    })

    customer_list_resp = api.model('customer_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'customers':fields.List(fields.Nested(customer))})

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