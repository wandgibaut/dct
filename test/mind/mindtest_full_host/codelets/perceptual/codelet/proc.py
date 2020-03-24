import json
import sys
import subprocess
import os
import redis
import time
from pymongo import MongoClient
import socket

root_codelet_dir='/home/codelet'

def getMemoryObjects(memory_name, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return getMongoMemory(entry['ip/port'], memory_name)
                elif entry['type'] == 'redis':
                    return getRedisMemory(convert_alt(entry['ip/port'])[0], convert(convert_alt(entry['ip/port'])[2])[0], convert(memory_name)[1])
                else:
                    return getTCPMemory(convert_alt(entry['ip/port'])[0], convert_alt(entry['ip/port'])[1], memory_name)
        return None


def setMemoryObjects(memory_name, field, value, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return setMongoMemory(entry['ip/port'], memory_name, field, value)
                elif entry['type'] == 'redis':
                    return setRedisMemory(convert_alt(entry['ip/port'])[0], convert(convert_alt(entry['ip/port'])[2])[0],convert(memory_name)[1], field, value)
                else:
                    return setTCPMemory(convert_alt(entry['ip/port'])[0], convert_alt(entry['ip/port'])[1], memory_name, field, value)



def getRedisMemory(host, port, memory_name):
    client = redis.Redis(host=host, port=port)
    return json.loads(client.get(memory_name))


def setRedisMemory(host, port, memory_name, field, value):
    client = redis.Redis(host=host, port=port)
    mem = json.loads(client.get(memory_name))
    mem[field] = value
    client.set(memory_name, json.dumps(mem))


def getMongoMemory(host_port, memory_name):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert(memory_name)[0]]
    return collection.find_one({'name': convert(memory_name)[1]})
    

def setMongoMemory(host_port, memory_name, field, value):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert(memory_name)[0]]
    collection.update_one({'name': convert(memory_name)[1]}, {'$set': {field:value}})

def getTCPMemory(host, port, memory_name):
    data = 'get_' + memory_name
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,port))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return json.loads(received)

def setTCPMemory(host, port, memory_name, field, value):
    data = 'set_' + memory_name + '_' + field + '_' + value
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,port))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return received


def convert(string): 
    li = list(string.split("/")) 
    return li 

def convert_alt(string): 
    li = list(string.split(":")) 
    return li 


def main(activation):
    mem = getMemoryObjects('perceptual-input-memories/sensory-memory', 'inputs')
    I = mem['I']
    setMemoryObjects('behavioral-input-memories/perceptual-memory', 'I', I, 'outputs')

    
 


if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

