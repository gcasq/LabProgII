import requests
import pymongo
import json

url = 'https://jsonplaceholder.typicode.com/users'
params = {'limit': 16, 'country': 'us', 'apikey': 'API-KEY'}
#response = requests.get(url, params=params,stream=True)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["user_python"]
mycol = mydb["teste"]

#for i in response.json():
 #   x = mycol.insert_one(i)



def create():
    print("Type the dictionary you want to insert")
    dic_aux = input()
    json_acceptable_string = dic_aux.replace("'", "\"")
    try: 
        d = json.loads(json_acceptable_string)
        x = mycol.insert_one(d)
        print("document created with success, _id: ",x.inserted_id)          
    except ValueError as e: 
        print ("Not a valid JSON. Try again") 

def read():
    print('type your query in dic format, empty curly brackets to read all: ')
    query = input()
    json_acceptable_string = query.replace("'", "\"")
    try: 
        query_dic = json.loads(json_acceptable_string)
        for x in mycol.find(query_dic):
            print(x)
    except ValueError as e: 
        print ("Not a valid JSON. Try again")

def update():
    print("Select the id of the user you want to update: ")
    id=int(input())
    for x in mycol.find({'id':id}):
        print(x)
    myquery = { "id": int(id) }
    print("Digite o dicionário que quer substituir: ")
    print("Para campos aninhados, coloque \'field1.field2\':\'new value\'")
    dic_aux = input()
    json_acceptable_string = dic_aux.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    newvalues = { "$set": d }
    print("Update all? (y/n)")
    answer = input()
    if answer == 'y':
        x = mycol.update_many(myquery, newvalues)
        print(x.modified_count, "documents updated.")
        return

    x = mycol.update_one(myquery, newvalues)
    print(x.modified_count, "documents updated.")

def delete():
    print("Select the id of the user you want to delete: ")
    id = input()
    
    print("Delete all? (y/n)")
    answer = input()
    if answer == 'y':
        x = mycol.delete_many({"id": int(id)})
        print(x.deleted_count, " documents deleted.") 
        return
    
    x = mycol.delete_one({"id": int(id)})
    print(x.deleted_count, " documents deleted.") 
        
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