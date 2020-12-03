import requests
import pymongo
url = 'https://jsonplaceholder.typicode.com/users'
params = {'limit': 16, 'country': 'us', 'apikey': 'API-KEY'}

response = requests.get(url, params=params,stream=True)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["user_python"]
mycol = mydb["teste"]

for i in response.json():
    x = mycol.insert_one(i)

def create():
    pass

def read():
    print("Select the id of the user you want to read: ")
    id = input()
    for x in mycol.find({},{"id": id}):
        print(x)

def update():
    pass

def delete():
    pass

while True:
    print("Select your action: ")
    print("1 - Create")
    print("2 - Read")
    print("3 - Update")
    print("4 - Delete")
    print("-1 - Sair")

    option = input()

    if option == '1':
        create()
    elif option == '2':
        read()
    elif option == '3':
        update()
    elif option == '4':
        delete()
    elif option =='-1':
        break