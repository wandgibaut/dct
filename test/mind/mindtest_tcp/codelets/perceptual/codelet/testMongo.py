from pymongo import MongoClient

# cliente = MongoClient('localhost', 27017)



cliente = MongoClient('mongodb://localhost:27017/')

banco = cliente['database-raw-memory']

outMem = banco['testCodelet-output-memories']

memory = {
    #'_id': '12345',
    'name': 'none',
    'ip/port': '127.0.0.1:8080',
    'isAnObject': 'false',
    'I': {},
    'eval': '0.0'
}





#mem_id = outMem.insert_one(memory).inserted_id
#print(mem_id)
outMem.update_one({'_id': '12345'}, {'$set': {'I':0}})


print(outMem.find_one({"_id": "12345"}))