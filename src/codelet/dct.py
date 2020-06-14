#*****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the MIT License                       #
# which accompanies this distribution, and is available at                    #
# https://opensource.org/licenses/MIT                                         #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
#*****************************************************************************#
import json
import sys
import redis
from pymongo import MongoClient
import socket
import socketserver


def getMemoryObjects(root_codelet_dir, memory_name, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return getMongoMemory(entry['ip/port'], memory_name)
                elif entry['type'] == 'redis':
                    return getRedisMemory(entry['ip/port'], convert("/", memory_name)[1])
                else:
                    #print(convert(":", entry['ip/port'])[0])
                    return getTCPMemory(convert(":", entry['ip/port'])[0], convert(":", entry['ip/port'])[1], memory_name)
        return None


def setMemoryObjects(root_codelet_dir, memory_name, field, value, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return setMongoMemory(entry['ip/port'], memory_name, field, value)
                elif entry['type'] == 'redis':
                    return setRedisMemory(entry['ip/port'], convert("/", memory_name)[1], field, value)
                else:
                    return setTCPMemory(convert(":", entry['ip/port'])[0], convert(":", entry['ip/port'])[1], memory_name, field, value)


def getMemoryObjectsGroup(root_codelet_dir, memory_name, inputOrOutput, group):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if group in entry['group']:
                getMemoryObjects(root_codelet_dir, memory_name, inputOrOutput)


def setMemoryObjectsGroup(root_codelet_dir, memory_name, field, value, inputOrOutput, group):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if group in entry['group']:
                setMemoryObjects(root_codelet_dir, memory_name, field, value, inputOrOutput)

def getRedisMemory(host_port, memory_name):
    host = convert(':',host_port)[0]
    port = convert(':',host_port)[1]
    client = redis.Redis(host=host, port=port)
    return json.loads(client.get(memory_name))


def setRedisMemory(host_port, memory_name, field, value):
    host = convert(':',host_port)[0]
    port = convert(':',host_port)[1]
    client = redis.Redis(host=host, port=port)
    mem = json.loads(client.get(memory_name))
    mem[field] = value
    client.set(memory_name, json.dumps(mem))


def getMongoMemory(host_port, memory_name):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert("/", memory_name)[0]]
    return collection.find_one({'name': convert("/", memory_name)[1]})
    

def setMongoMemory(host_port, memory_name, field, value):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert("/", memory_name)[0]]
    collection.update_one({'name': convert("/", memory_name)[1]}, {'$set': {field:value}})

def getTCPMemory(host, port, memory_name):
    data = 'get_' + memory_name
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return json.loads(received)

def setTCPMemory(host, port, memory_name, field, value):
    data = 'set_' + memory_name + '_' + field + '_' + value
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return received


def convert(separator, string): 
    li = list(string.split(separator)) 
    return li 


