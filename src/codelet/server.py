#*****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the GNU Lesser Public License v3      #
# which accompanies this distribution, and is available at                    #
# http://www.gnu.org/licenses/lgpl.html                                       #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
#*****************************************************************************#

import socketserver
import sys
import json

root_codelet_dir='/home/codelet'

class MyTCPHandler(socketserver.BaseRequestHandler):
    def getMemory(self, memory_name):
        with open(root_codelet_dir + '/memories/' +memory_name + '.json', 'r+') as json_data:
            memory = json.dumps(json.load(json_data))
            return memory


    def setMemory(self, memory_name, field, value):
        with open(root_codelet_dir + '/memories/' +memory_name + '.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = value
            json_data.seek(0) #rewind
            json.dump(jsonData, json_data)
            json_data.truncate()
            print(jsonData)

                                            

    def convert(self, string): 
        li = list(string.split("_")) 
        return li 

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        list_data = self.convert(self.data.decode())
        if(list_data[0] == 'get'):
            print(self.getMemory(list_data[1]))
            self.request.sendall(bytes(self.getMemory(list_data[1]), "utf-8"))
            
        if(list_data[0] == 'set'):
            self.setMemory(list_data[1], list_data[2], list_data[3])
            self.request.sendall(bytes('success!', "utf-8"))


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2:
        HOST= args[0]
        PORT  = int(args[1])
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    else:
        print(len(args))
        print('Error! Wrong number of arguments!')
        sys.exit()

    