import json
import sys
import subprocess
import os
import redis
import time
from pymongo import MongoClient


def main(activation):
    client = redis.Redis(host='redis', port=6379)
    init = time.time_ns()

    print('e')
    if (client.get('perceptual-memory') != None):
        print('f')
        mem = json.loads(client.get('perceptual-memory'))
        I = mem['I']
        if(client.get('behavioral-memory') != None):
            print('g')
            outMem = json.loads(client.get('behavioral-memory'))
            outMem['I']  = I
            client.set('behavioral-memory', json.dumps(outMem))
        else:
            print('h')
            newMem = {'name': 'behavioral','ip/port': 'redis://redis:6379/','type': 'redis','I': I,'eval': 0.0}
            client.set('behavioral-memory', json.dumps(newMem))

    print((time.time_ns() - init))


    
    
 


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

