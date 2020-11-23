from operator import and_
from db import db


class ItemModel(db.Model):
    """
    Item model
    """
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        """
        Ham khoi tao item
        """
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """
        Tra ve item json format
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'store_id': self.store_id
        }

    @classmethod
    def find_by_name(cls, name):
        # select * from items where name = name
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        """
        Trả về tất cả items
        """
        return cls.query.all()
    
    @classmethod
    def find_by_price(cls, params):
        """
        Trả về tất cả items trong tầm giá
        """
        min_price = params.get('min_price', default=0, type=int)
        max_price = params.get('max_price', default=999999, type=int)
        page = params.get('page', default=1, type=int)
        per_page = 10
        return cls.query.filter(and_(cls.price >= min_price, cls.price <= max_price)).paginate(page,per_page,error_out=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
