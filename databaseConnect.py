from pymongo import MongoClient


host = "mongodb://localhost:27017/"




# Create a MongoDB client object
client = MongoClient(host)


# def Query(database, collection, dataTitleList, dataList):
#     db = client[database]
#     col = db[collection]
#     new_doc = {}

#     for i in range(len(dataTitleList)):
#         new_doc[dataTitleList[i]] = dataList[i]

#     result = col.insert_one(new_doc)
#     return result


def DeleteOne(database, collection, filter : dict):
    db = client[database]
    col = db[collection]
   # Delete a single document matching a specific condition
    delete_result = collection.delete_one(filter)
def DeleteAllOf(database, collection, filter : dict):
    db = client[database]
    col = db[collection]
   # Delete a single document matching a specific condition
    delete_result = collection.delete_many(filter)

def Insert(database, collection, new_document : dict):
    db = client[database][collection]
    db.insert_one(new_document)

def InsertStack(database, collection, new_document : list):
    db = client[database][collection]
    db.insert_many(new_document)

def Search(database, collection, filter : dict):
    db = client[database]
    col = db[collection]

    result = col.find(filter)
    return result