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
    inMem = base['behavioral-input-memories']

    outMem = base['motor-input-memories']


    mem = inMem.find_one({'_id': '123456'})
    if (mem != None):
        I = mem['I']
        newMem = outMem.find_one({'_id': '123456'})
        if(newMem != None):
            outMem.update_one({'_id': '123456'}, {'$set': {'I':I}})
        else:
            outMem.insert_one(mem)

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

