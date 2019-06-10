from flask import Flask, jsonify, request, render_template
# from flask package import class Flask
# jsonify method takes in a map/dict in python and return a json string
# request

app = Flask(__name__)

# stores list, contains one store map { 'name': 'my store', 'items': []},
# items list contains map {'name': 'my item', 'price': 15.99}
stores = [
    {
        'name': 'my store',
        'items': [
            {
               'name': 'my item',
                'price': 15.99
            }
        ]
    }
]


# home page visit
@app.route('/')
def home():
    return render_template('index.html')

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  # get data from the post request
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message': 'store not found'})  # always return a map and jsonify it


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # jsonify only take in map


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    # suppose the store exists
    request_data = request.get_json()
    item_name = request_data['name']
    price = request_data['price']
    for store in stores:
        if store['name'] == name:
            new_item = {'name': item_name, 'price': price}
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)





