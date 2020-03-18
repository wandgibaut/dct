import json
import sys
import subprocess
import os
import redis
import time
from pymongo import MongoClient


def main(activation):
    init = time.time_ns()
    client = redis.Redis(host='redis', port=6379)
    #client = MongoClient('mongodb://mongodb:27017/')
    #base = client['database-raw-memory']
    #outMem = base['perceptual-input-memories']

    mem = client.get('sensory-memory')

    if(mem == None):
        memory = {'name': 'sensory','ip/port': 'redis://redis:6379/','type': 'redis','I': 0,'eval': 0.0}
        j_memory = json.dumps(memory)
        #client.hmset('sensory-memory',memory)
        client.set('sensory-memory',j_memory)

    #mem = client.hgetall('sensory-memory')
    mem = json.loads(client.get('sensory-memory'))
    print(mem)
    I = int(mem['I'])
    I +=1
    mem['I'] = str(I)
    client.set('sensory-memory',json.dumps(mem))

    print((time.time_ns() - init))
    #outMem.update_one({'name': 'sensory'}, {'$set': {'I':I+1}})


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

