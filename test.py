# if __name__ == '__main__':
#     # set = {2, 3, 5}
#     # print(set)
#     # persons = ["Ann", "Frank", "John"]
#     # person = input("enter the person you know: ")
#     # if person in persons:
#     #     print(" you know {} ".format(person))
#     # else:
#     #     print("you don't know this person")
#
#     # def who_do_you_know():
#     #     name_input = input("input all your friends:")
#     #     name_list = [name.strip() for name in name_input.split()]
#     #
#     #     return name_list
#     #
#     # def ask_user():
#     #     name = input("input a name: ")
#     #     name_list = who_do_you_know()
#     #     if name in name_list:
#     #         print("you know {}".format(name))
#
#     class Student:
#         def __init__(self, name, school):
#             self.name = name
#             self.school = school
#             self.mark = []
#
#         def mark_avg(self):
#             avg = sum(self.mark)/len(self.mark)
#             return avg
#
#         @classmethod
#         def friend(cls, student_origin, friend_name, *args, **kwargs):
#             return cls(friend_name, student_origin.school, *args, **kwargs)
#
#     class WorkingStudent(Student):  # inheritance, super class: Student
#         def __init__(self, name, school, salary):
#             super().__init__(name, school)
#             self.salary = salary
#
#
#     # anna = WorkingStudent('Anna', 'MIT', 20.00)
#     #
#     # print(anna.salary)
#     # greg = WorkingStudent.friend(anna, 'Greg', 25.00)
#     # print(greg.name)
#     #
#     # anna.mark.append(56)
#     # print(anna.mark_avg())
#
# # class Store with string name and items list(empty)
# # func add_item(self, item_name, price) which is a map 'name' : item_name and 'price' : price
# # func stock_total(self) return the sum of the total price of all items in that store
# # class method franchise(cls, store) return a new store with Name + " - franchise"
# # static method store_details(store) return "Name, total stock price: Total Price"
#
#     class Store:
#         def __init__(self, name):
#             self.name = name
#             self.items = []
#
#         def add_item(self, name, price):
#             self.items.append({
#                 'name': name,
#                 'price': price
#             })
#
#         def stock_total(self):
#             return sum((item['price'] for item in self.items))
#
#         @classmethod
#         def franchise(cls, store):
#             return cls(store.name + " - franchise")
#
#         @staticmethod
#         def store_details(store):
#             return "{}, total stock price: {}".format(store.name, int(store.stock_total()))
#
#     store = Store("test")
#     store_1 = Store("Amazon")
#     store_1.add_item("keyboard", 160)
#
#     Store.franchise(store)
#     Store.franchise(store_1)
#
#     Store.store_details(store)
#     Store.store_details(store_1)
#
#     nums = [2, 3, 4, 5]
#     print(filter(lambda x: x % 2 != 0, nums))
#     print(list(filter(lambda x: x % 2 != 0, nums)))
#     print([num for num in nums if num % 2 != 0])


from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name': 'my item', 'price': 15.99}]
}]


# @app.route('/')
# def home():
#     return render_template('index.html')


# post /store data: {name :}
@app.route('/store', methods=['POST'])
def create_store():
    # request_data = request.get_json()
    # new_store = {
    #     'name': request_data['name'],
    #     'items': []
    # }
    # stores.append(new_store)
    # return jsonify(new_store)
    pass


# get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    # for store in stores:
    #     if store['name'] == name:
    #         return jsonify(store)
    # return jsonify({'message': 'store not found'})
    pass


# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    # pass


# post /store/<name> data: {name :}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    # request_data = request.get_json()
    # for store in stores:
    #     if store['name'] == name:
    #         new_item = {
    #             'name': request_data['name'],
    #             'price': request_data['price']
    #         }
    #         store['items'].append(new_item)
    #         return jsonify(new_item)
    # return jsonify({'message': 'store not found'})
    pass


# get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    # for store in stores:
    #     if store['name'] == name:
    #         return jsonify({'items': store['items']})
    # return jsonify({'message': 'store not found'})

    pass


app.run(debug=True,host='0.0.0.0',port=5000)

