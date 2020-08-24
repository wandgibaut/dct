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

import socketserver
import sys
import json
import threading
import os
import glob

root_node_dir = os.getenv('ROOT_NODE_DIR')


class CodeletTCPHandler(socketserver.BaseRequestHandler):
    # TODO: improve
    def get_memory(self, memory_name):
        file_memory = None
        for filename in glob.iglob(root_node_dir + '/**', recursive=True):
            if filename.__contains__(memory_name + '.json'):
                file_memory = filename
        with open(file_memory, 'r+') as json_data:
            memory = json.dumps(json.load(json_data))
            return memory

    def set_memory(self, memory_name, field, value):
        file_memory = None
        for filename in glob.iglob(root_node_dir + '/**', recursive=True):
            if filename.__contains__(memory_name + '.json'):
                file_memory = filename
        with open(file_memory, 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = value
            json_data.seek(0) # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def get_codelet_info(self, codelet_name):
        file_fields = None
        for filename in glob.iglob(root_node_dir + '/**', recursive=True):
            if filename.__contains__(codelet_name + '/fields.json'):
                file_fields = filename
        with open(file_fields, 'r+') as json_data:
            fields = json.dumps(json.load(json_data))
            return fields

    @staticmethod
    def convert(string):
        li = list(string.split("_"))
        return li

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        list_data = self.convert(self.data.decode())
        if list_data[0] == 'get':
            self.request.sendall(bytes(self.get_memory(list_data[1]), "utf-8"))
            
        if list_data[0] == 'set':
            self.set_memory(list_data[1], list_data[2], list_data[3])
            self.request.sendall(bytes('success!', "utf-8"))

        if list_data[0] == 'info':
            print('Ok!')
            self.request.sendall(bytes(self.get_codelet_info(list_data[1]), "utf-8"))


def split(string): 
    li = list(string.split(":")) 
    return li 


if __name__ == "__main__":
    args = sys.argv[1:]
    HOST = split(args[0])[0]
    PORT = int(split(args[0])[1])
    server = socketserver.TCPServer((HOST, PORT), CodeletTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    threading.Thread(target=server.serve_forever).start()
    # server.serve_forever()
