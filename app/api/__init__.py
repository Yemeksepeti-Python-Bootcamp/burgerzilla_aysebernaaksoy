from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .restaurants.controller import api as restaurants_ns

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.", title="API", description="API")


api.add_namespace(user_ns)
api.add_namespace(restaurants_ns)