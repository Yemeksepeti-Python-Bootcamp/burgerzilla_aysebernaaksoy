from app import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    detailed_info = db.Column(db.String(256))
    price = db.Column(db.String(32))
    image_url = db.Column(db.String(256))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

    def __repr__(self):
        return '<Product {}>'.format(self.name)