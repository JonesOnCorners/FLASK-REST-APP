from models.store import StoreModel
from flask_restful import Resource, reqparse


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_item_by_name(name=name)
        
        if store:
            return store.json()   
        return ({'message': f'Store [name={name}] not found'}), 404

    def post(self, name):
        store = StoreModel.find_item_by_name(name=name)

        if store:
            return ({'message': f'Store with [name={name}] already exists'}), 400

        store = StoreModel(name=name)
        
        try:
            store.save_to_db()
        except:
            return ({'message': f"An error occured while inserting Store [name={name}]"}), 500
        
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_item_by_name(name=name)

        if store:
            store.delete_from_db()
            return store.json(), 200
        else:
            return ({'message':f"Store with [name={name}] not found"}), 500

    
    def put(self, name):
        store = StoreModel.find_item_by_name(name=name)

        updated_store = StoreModel(name=name)
        
        if not store:
            try:
                updated_store.insert()
            except:
                return ({'message':f'Error inserting store with [name={name}]'}), 500
        
        try:
            updated_store.update()
        except:
            return ({'message':f'Error updating store with [name={name}]'}), 500
        
        return updated_store.json()


class StoreList(Resource):

    def get(self):
        return StoreModel.find_all_items()
        















