import json
import sys
import subprocess
import os
import redis
import pickle
from pymongo import MongoClient


def main(activation):
    client = redis.Redis(host='redis', port=6379)

    if (client.get('behavioral-memory') != None):
        mem = pickle.loads(client.get('behavioral-memory'))
        I = mem['I']
        print(I)


    
    
 


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

