from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    """
    Tạo resource cho Store
    """

    def get(self, name):
        """
        HTTP GET
        """
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        """
        HTTP POST
        """
        if StoreModel.find_by_name(name):
            return {'message': f"A store with name '{name}' already exists."}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store'}, 500
        return store.json()

    def delete(self, name):
        """
        HTTP DEL
        """
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message': 'Store deleted'}


class StoreList(Resource):
    """
    List store
    """
    def get(self):
        """
        GET list store
        """
        return {'stores': [store.json() for store in StoreModel.query.all() ]}
