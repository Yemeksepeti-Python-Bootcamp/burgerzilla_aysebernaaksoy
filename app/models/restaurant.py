from app import db
import random

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    restaurantmenu = db.relationship("Menu", backref="restaurants", lazy="dynamic")

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)

    @staticmethod
    def insert_restaurant():
        default_restaurant = Restaurant(name='Dombili '+str(random.randint(0,100)), user_id=1)
        db.session.add(default_restaurant)
        db.session.commit()
        default_restaurant2 = Restaurant(name='Dublemumble '+str(random.randint(0,100)), user_id=2)
        db.session.add(default_restaurant2)
        db.session.commit()