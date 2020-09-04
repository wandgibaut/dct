# ****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
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
import sys
import os
import time
import socket
import socketserver
import redis
from pymongo import MongoClient


class PythonCodelet:
    def __init__(self, name=None, root_codelet_dir=None):
        if root_codelet_dir is None:
            os.chdir(os.path.dirname(__file__))
            root_codelet_dir = os.getcwd()
        self.root_codelet_dir = root_codelet_dir
        self.name = name

    def read_field(self, field):
        with open(self.root_codelet_dir + '/fields.json', 'r') as json_data:
            jsonData = json.load(json_data)
            value = jsonData[field]
        return value

    def change_field(self, field, value):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = value
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def add_entry(self, field, data):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            vector = jsonData[field]
            vector.append(json.loads(data))
            jsonData[field] = vector

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def remove_entry(self, field, name):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            vector = jsonData[field]

            for i in vector:
                for k, v in i.items():
                    if v == name:
                        vector.remove(i)
                        return i

            jsonData[field] = vector
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def set_field_list(self, field, dataList):
        jsonList = []
        for dataString in dataList:
            jsonList.append(json.loads(dataString))

        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = jsonList
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    @staticmethod
    def convert(self, string):
        li = list(string.split(";"))
        return li

    def run(self):
        while self.read_field('enable') == 'true':
            while self.read_field('lock') == 'false':
                activation = self.calculate_activation()
                self.proc(activation)
                time.sleep(float(self.read_field('timestep')))

        sys.exit()

    def calculate_activation(self):
        ########################################
        # Default Activation ##
        print("default activation")
        return 0

    def proc(self, activation):
        ########################################
        # Default proc ##
        print("default proc")


def get_memory_objects(root_codelet_dir, memory_name, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return get_mongo_memory(entry['ip/port'], memory_name)
                elif entry['type'] == 'redis':
                    return get_redis_memory(entry['ip/port'], convert("/", memory_name)[1])
                elif entry['type'] == 'tcp':
                    return get_tcp_memory(convert(":", entry['ip/port'])[0], convert(":", entry['ip/port'])[1],
                                          memory_name)
                else:
                    return get_local_memory(entry['ip/port'], entry['name'])

        return None


def set_memory_objects(root_codelet_dir, memory_name, field, value, inputOrOutput):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if entry['name'] == memory_name:
                if entry['type'] == 'mongo':
                    return set_mongo_memory(entry['ip/port'], memory_name, field, value)
                elif entry['type'] == 'redis':
                    return set_redis_memory(entry['ip/port'], convert("/", memory_name)[1], field, value)
                elif entry['type'] == 'tcp':
                    return set_tcp_memory(convert(":", entry['ip/port'])[0], convert(":", entry['ip/port'])[1],
                                          memory_name, field, value)
                else:  # local
                    return set_local_memory(entry['ip/port'], memory_name, field, value)


def get_memory_objects_group(root_codelet_dir, inputOrOutput, group):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        answer = []
        for entry in vector:
            if group in entry['group']:
                answer.append(get_memory_objects(root_codelet_dir, entry['name'], inputOrOutput))
        if answer:
            return answer
        return None


def set_memory_objects_group(root_codelet_dir, field, value, inputOrOutput, group):
    with open(root_codelet_dir + '/fields.json', 'r+') as json_data:
        jsonData = json.load(json_data)
        vector = jsonData[inputOrOutput]
        for entry in vector:
            if group in entry['group']:
                set_memory_objects(root_codelet_dir, entry['name'], field, value, inputOrOutput)


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
    data = 'get_' + memory_name
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return json.loads(received)


def set_tcp_memory(host, port, memory_name, field, value):
    data = 'set_' + memory_name + '_' + field + '_' + value
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        return received


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


def add_memory_to_group(root_codelet_dir, memory_name, newGroup, inputOrOutput):
    memory_group = get_memory_objects(root_codelet_dir, memory_name, inputOrOutput)['group']
    memory_group.append(newGroup)
    set_memory_objects(root_codelet_dir, memory_name, 'group', memory_group, inputOrOutput)


def get_codelet_info(host, port):
    data = 'info_'
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
