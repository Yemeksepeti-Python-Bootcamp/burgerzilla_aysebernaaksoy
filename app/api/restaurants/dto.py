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