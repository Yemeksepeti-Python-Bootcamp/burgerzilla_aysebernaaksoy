def load_restaurant_data(restaurant_db_obj):
    from app.models.schemas import RestaurantSchema
    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(restaurant_db_obj)
    return data

def load_menu_data(menu_db_obj):
    from app.models.schemas import MenuSchema
    menu_schema = MenuSchema()
    data = menu_schema.dump(menu_db_obj)
    return data