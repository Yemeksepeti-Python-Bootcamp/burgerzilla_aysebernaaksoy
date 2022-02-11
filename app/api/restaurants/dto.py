from flask_restx import Namespace,fields
from constants.texts import Texts
class RestaurantDto:
    api = Namespace(Texts.TABLE_NAME_RESTAURANT, description=Texts.RESTAURANT_DTO_DESC)
    restaurant = api.model(Texts.TABLE_NAME_RESTAURANT, {
        'id':fields.Integer,
        'name':fields.String,
        'user_id':fields.Integer,
    })

    restaurant_resp = api.model(Texts.RESTAURANT_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurant':fields.Nested(restaurant)
    })

    restaurant_list_resp = api.model(Texts.RESTAURANT_LIST_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurants':fields.List(fields.Nested(restaurant))})

    menu = api.model(Texts.TABLE_NAME_MENU, {
        'id':fields.Integer,
        'name':fields.String,
        'restaurant_id':fields.Integer,
    })

    product = api.model(Texts.TABLE_NAME_PRODUCT, {
        'id':fields.Integer,
        'name':fields.String,
        'detailed_info':fields.String,
        'price':fields.String,
        'image_url':fields.String,
        'menu_if':fields.Integer
    })
    product_resp = api.model(Texts.PRODUCT_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'product':fields.Nested(product)
    })

    order = api.model(Texts.TABLE_NAME_ORDER, {
        'id':fields.Integer,
        'no':fields.String,
        'status':fields.String,
        'items':fields.String
    })

    order_resp = api.model(Texts.ORDER_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'orders':fields.List(fields.Nested(order))})