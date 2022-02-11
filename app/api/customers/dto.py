from flask_restx import Namespace,fields
from constants.texts import Texts
class CustomerDto:
    api = Namespace(Texts.TABLE_NAME_CUSTOMER, description=Texts.CUSTOMER_DTO_DESC)
    customer = api.model(Texts.TABLE_NAME_CUSTOMER, {
        'id':fields.Integer,
        'no':fields.String,
        'restaurant_id':fields.Integer,
        'user_id':fields.Integer,
        'menu_id':fields.Integer,
        'status':fields.String
    })

    customer_resp = api.model(Texts.CUSTOMER_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'customer':fields.Nested(customer)
    })

    customer_list_resp = api.model(Texts.CUSTOMER_LIST_RESP_DESC, {
        'status':fields.Boolean,
        'message':fields.String,
        'customers':fields.List(fields.Nested(customer))})