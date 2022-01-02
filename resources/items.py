from models.item import ItemModel
from flask_restful import Resource, reqparse


class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Item price cannot be blank"
    )

    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Store ID cannot be blank"
    )

    def get(self, name):
        item = ItemModel.find_item_by_name(name=name)
        
        if item:
            return item.json()   
        return ({'message': f'Item [name={name}] not found'}), 404

    def post(self, name):
        item = ItemModel.find_item_by_name(name=name)

        if item:
            return ({'message': f'Item with [name={name}] already exists'}), 400

        data = Item.parser.parse_args()

        item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
                
        try:
            item.save_to_db()
        except:
            return ({'message': f"An error occured while inserting item [name={name}, price={data['price']}]"}), 500
        
        return item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_item_by_name(name=name)

        if item:
            item.delete_from_db()
            return item.json(), 200
        else:
            return ({'message':f"Item with [name={name}] not found"}), 500

    
    def put(self, name):
        item = ItemModel.find_item_by_name(name=name)

        data = Item.parser.parse_args()

        updated_item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
        
        if not item:
            try:
                updated_item.insert()
            except:
                return ({'message':f'Error inserting item with [name={name}]'}), 500
        
        try:
            updated_item.update()
        except:
            return ({'message':f'Error updating item with [name={name}]'}), 500
        
        return updated_item.json()



class ItemList(Resource):

    def get(self):
        return ItemModel.find_all_items()
        















