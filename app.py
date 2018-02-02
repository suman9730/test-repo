#Import Section starts

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

#Import Section ends

app = Flask(__name__)
app.secret_key = 'keyapi'
api = Api(app)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                            type=float,
                            required=True,
                            help="Mandatory field")
    
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):

        #if next(filter(lambda x: x['name'] == name, items), None):
        #   return{'message': 'Item already exists'}, 400           

        #data = request.get_json()
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 
    
class ItemList(Resource):
    def get(self):
        return {'items': items}
    
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
