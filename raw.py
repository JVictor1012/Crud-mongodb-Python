from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
db_connection = client["teste"]

print(db_connection)

collection = db_connection.get_collection("collection1")

print(collection)

search_filter = {
    "ola": "mundo"
}

response = collection.find(search_filter)

print()

for registry in response:
    
    print(registry)
    
collection.insert_one({
    "name": "jão",
    "age": "20",
    "email": ""
})


