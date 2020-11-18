from db import db


class StoreModel(db.Model):
    """
    Store model
    """
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #load các đối tượng liên quan

    def __init__(self, name):
        """
        Ham khoi tao item
        """
        self.name = name

    def json(self):
        """
        Tra ve item json format
        """
        return {'name': self.name, 'items': [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from tableName where name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
