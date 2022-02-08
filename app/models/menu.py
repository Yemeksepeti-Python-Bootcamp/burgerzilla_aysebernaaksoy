from app import db

class Menu(db.Model):
    __tablename__ = 'menu'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    detailed_info = db.Column(db.String(256))
    price = db.Column(db.String(32))
    image_url = db.Column(db.String(256))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def __repr__(self):
        return '<Menu {}>'.format(self.name)