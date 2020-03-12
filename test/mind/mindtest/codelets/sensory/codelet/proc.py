import json
import sys
import subprocess
import os
from pymongo import MongoClient


def main(activation):
    #output = json.dumps(list(list(subprocess.check_output("./getOutput.sh").split('['))[1].split(']'))[0])
    #print(output)

    # cliente = MongoClient('localhost', 27017)

    client = MongoClient('mongodb://mongodb:27017/')
    base = client['database-raw-memory']

    outMem = base['perceptual-input-memories']

    mem = outMem.find_one({'_id': '123456'})

    if(mem == None):
        memory = {'name': 'none','ip/port': '127.0.0.1:8080','isAnObject': 'false','I': 0,'eval': '0.0', '_id': '123456'}
        outMem.insert_one(memory)

    
    mem = outMem.find_one({'_id': '123456'})

    I = mem['I']
    print(I)

    outMem.update_one({'_id': '123456'}, {'$set': {'I':I+1}})


    #cmd2 = "../accessMemoryObjects.sh"
    #value = int(subprocess.check_output([cmd2,"read", "simpleMemory", "I"]))

    #cmd = "../accessMemoryObjects.sh"
    #subprocess.call([cmd,"mod", "simpleMemory", "I", str(value+1)])
    
    
 


def convert(string): 
    li = list(string.split(", ")) 
    return li 



if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

