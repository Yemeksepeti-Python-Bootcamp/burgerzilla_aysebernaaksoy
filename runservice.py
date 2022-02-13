import os
import click
import random
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_migrate import Migrate
from app import create_app, db
from app.models.user import User
from app.models.restaurant import Restaurant
from app.models.menu import Menu
from app.models.product import Product
from app.models.order import Order
from app.models.order_detail import OrderDetail

app = create_app(os.getenv("FLASK_CONFIG") or "default")

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """Make database operations with shell, without import db"""
    return dict(db=db, User=User, Restaurant=Restaurant, Menu=Menu, Product=Product, Order=Order, OrderDetail=OrderDetail)

# with app.app_context():
#     #User.insert_user()
#     default_user = User(name='customer1'+str(random.randint(0,100)), username='customer1'+str(random.randint(0,100)), email='customer1@customer.com'+str(random.randint(0,100)), password='12345678')
#     db.session.add(default_user)
#     db.session.commit()

#     default_user = User(name='user1'+str(random.randint(0,100)), username='user1'+str(random.randint(0,100)), email='user1@user.com'+str(random.randint(0,100)), password='12345678')
#     db.session.add(default_user)
#     db.session.commit()
#     Restaurant.insert_restaurant()
#     Menu.insert_menu()
#     Product.insert_product()


@app.cli.command()
def initialvalues():
    from app.models.user import User
    from app.models.restaurant import Restaurant
    from app.models.menu import Menu
    from app.models.product import Product
    """Run flask initialvalues : creating initial datas """
    User.insert_user()
    Restaurant.insert_restaurant()
    Menu.insert_menu()
    Product.insert_product()
    return 1

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit test """
    import unittest

    if test_names:
        """
        flask test tests.test_dataset_model
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests',pattern='test*.py')

    result =  unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1