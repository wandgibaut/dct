import json
import sys
import subprocess
import os
import redis
import pickle
from pymongo import MongoClient


def main(activation):
    client = redis.Redis(host='redis', port=6379)

    
    print('a')
    if (client.get('sensory-memory') != None):
        print('b')
        mem = pickle.loads(client.get('sensory-memory'))
        I = mem['I']
        if(client.get('perceptual-memory') != None):
            outMem = pickle.loads(client.get('perceptual-memory'))
            outMem['I'] +=1
            client.set('perceptual-memory', pickle.dumps(outMem))
        else:
            newMem = {'name': 'perceptual','ip/port': 'redis://redis:6379/','type': 'redis','I': I,'eval': 0.0}
            client.set('perceptual-memory', pickle.dumps(newMem))


    
 


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

