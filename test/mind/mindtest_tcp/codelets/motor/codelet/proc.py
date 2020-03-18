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
	print('i')
	
	if(client.get('behavioral-memory') != None):
		print('j')
		mem = json.loads(client.get('behavioral-memory'))
		I = mem['I']
		print(I)

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

