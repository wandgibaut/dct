# ****************************************************************************#
# Copyright (c) 2022  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the MIT License                       #
# which accompanies this distribution, and is available at                    #
# https://opensource.org/licenses/MIT                                         #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
# ****************************************************************************#

import json
import re
import requests
import socket
import redis
from pymongo import MongoClient
from dct import codelets
from dct import parser
from dct import server

__version__ = '0.1.0'
__author__ = 'Wandemberg Gibaut'


def get_memory_object(memory_name, ip_port, conn_type):
    if conn_type == 'mongo':
        return get_mongo_memory(ip_port, memory_name)
    elif conn_type == 'redis':
        return get_redis_memory(ip_port, convert("/", memory_name)[1])
    elif conn_type == 'tcp':
        return get_tcp_memory(convert(":", ip_port)[0], convert(":", ip_port)[1], memory_name)
    elif conn_type == 'local':
        return get_local_memory(ip_port, memory_name)
    return None

#TODO: change TCP method
def set_memory_object(memory_name, ip_port, conn_type, field, value):
    if conn_type == 'mongo':
        return set_mongo_memory(ip_port, memory_name, field, value)
    elif conn_type == 'redis':
        return set_redis_memory(ip_port, convert("/", memory_name)[1], field, value)
    elif conn_type == 'tcp':
        return set_tcp_memory(convert(":", ip_port)[0], convert(":", ip_port)[1], memory_name, field, value)
    elif conn_type == 'local':
        return set_local_memory(ip_port, memory_name, field, value)
    return None


def get_memory_objects_by_name(root_codelet_dir, memory_name, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        answer = []
        for entry in vector:
            if entry['name'] == memory_name:
                answer.append(get_memory_object(memory_name, entry['ip/port'], entry['type']))
        if len(answer) != 0:
            return answer
        return None


def set_memory_objects_by_name(root_codelet_dir, memory_name, field, value, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                set_memory_object(memory_name, entry['ip/port'], entry['type'], field, value)
        return 0


def get_memory_objects_by_group(root_codelet_dir, group, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        answer = []
        for entry in vector:
            if group in entry['group']:
                answer.append(get_memory_object(entry['name'], entry['ip/port'], entry['type']))
        if len(answer) != 0:
            return answer
        return None


def set_memory_objects_by_group(root_codelet_dir, group, field, value, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if group in entry['group']:
                set_memory_object(entry['name'], entry['ip/port'], entry['type'], field, value)
        return 0


def get_all_memory_objects(root_codelet_dir, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        answer = []
        for entry in vector:
            answer.append(get_memory_object(entry['name'], entry['ip/port'], entry['type']))
        if len(answer) != 0:
            return answer
        return None


def get_redis_memory(host_port, memory_name):
    host = convert(':', host_port)[0]
    port = convert(':', host_port)[1]
    client = redis.Redis(host=host, port=port)
    return json.loads(client.get(memory_name))


def set_redis_memory(host_port, memory_name, field, value):
    host = convert(':', host_port)[0]
    port = convert(':', host_port)[1]
    client = redis.Redis(host=host, port=port)
    mem = json.loads(client.get(memory_name))
    mem[field] = value
    client.set(memory_name, json.dumps(mem))


def get_mongo_memory(host_port, memory_name):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert("/", memory_name)[0]]
    return collection.find_one({'name': convert("/", memory_name)[1]})


def set_mongo_memory(host_port, memory_name, field, value):
    client = MongoClient(host_port)
    base = client['database-raw-memory']
    collection = base[convert("/", memory_name)[0]]
    collection.update_one({'name': convert("/", memory_name)[1]}, {'$set': {field: value}})


def get_tcp_memory(host, port, memory_name):
    #data = 'get_' + memory_name
    response = requests.get(f'http://{host}:{port}/get_memory/{memory_name}')
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
    #    sock.connect((host, int(port)))
    #    sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
    #    received = str(sock.recv(1024), "utf-8")
    #    return json.loads(received)
    return response.json()


def set_tcp_memory(host, port, memory_name, field, value):
    #data = 'set_' + memory_name + '_' + field + '_' + value
    response = requests.post(f'http://{host}:{port}/set_memory/', json={'memory_name': memory_name, 'field': field, 'value': value})
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #    # Connect to server and send data
    #    sock.connect((host, int(port)))
    #    sock.sendall(bytes(data + "\n", "utf-8"))
    #    # Receive data from the server and shut down
    #    received = str(sock.recv(1024), "utf-8")
    #    return received
    return response


def get_local_memory(path, memory_name):
    with open(path + '/' + memory_name + '.json', 'r+') as json_data:
        return json.load(json_data)


def set_local_memory(path, memory_name, field, value):
    with open(path + '/' + memory_name + '.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        jsonData[field] = value
        # print(jsonData[field])

        json_data.seek(0)  # rewind
        json.dump(jsonData, json_data)
        json_data.truncate()


#TODO: solve this issue
def add_memory_to_group(root_codelet_dir, memory_name, newGroup, inputOrOutput):
    memory_group = get_memory_objects_by_group(root_codelet_dir, memory_name, inputOrOutput)['group']
    memory_group.append(newGroup)
    set_memory_objects_by_name(root_codelet_dir, memory_name, 'group', memory_group, inputOrOutput)


def get_node_info(host, port):
    data = 'info'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print(received)
        try:
            answer = json.loads(received)
        except:
            answer = []
            raise Exception
        return answer

def get_codelet_info(host, port, codelet_name):
    data = 'info_' + codelet_name
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print(received)
        try:
            answer = json.loads(received)
        except:
            answer = []
            raise Exception
        return answer


def convert(separator, string):
    li = list(string.split(separator))
    return li