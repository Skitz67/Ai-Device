from pymongo import MongoClient

# Create a MongoDB client object
client = MongoClient()


def Query(database, collection, dataTitleList, dataList):
    #writes to database
    db = client[database]
    col = db[collection]
    new_doc = {}

    for i in range(len(dataTitleList)):
        new_doc[dataTitleList[i]] = dataList[i]

    result = col.insert_one(new_doc)
    return result


def Delete(database, collection, dataTitleList, dataList):
    #deletes from database
    db = client[database]
    col = db[collection]
    delete_criteria = {}

    for i in range(len(dataTitleList)):
        delete_criteria[dataTitleList[i]] = dataList[i]
        result = col.delete_one(delete_criteria)
    return result

def Search(database, collection, query, projection, options):
    #Reads from database
    db = client[database]
    col = db[collection]

    result = db.col.find(query, projection, options)
    return result
