import json
import sys
import subprocess
import os
from pymongo import MongoClient


def main(activation):
    client = MongoClient('mongodb://mongodb:27017/')
    base = client['database-raw-memory']
    inMem = base['perceptual-input-memories']
    outMem = base['behavioral-input-memories']

    mem = inMem.find_one({'name': 'sensory'})
    
    if (mem != None):
        I = mem['I']
        if(outMem.find_one({'name': 'perceptual'}) != None):
            outMem.update_one({'name': 'perceptual'}, {'$set': {'I':I}})
        else:
            newMem = {'name': 'perceptual','ip/port': 'mongodb://mongodb:27017/','type': 'mongo','I': I,'eval': 0.0}
            outMem.insert_one(newMem)


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

