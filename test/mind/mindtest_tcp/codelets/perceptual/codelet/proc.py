import json
import sys
import subprocess
import os
import redis
import time
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        
        client = redis.Redis(host='redis', port=6379)
        init = time.time_ns()
    
        #print('a')
        #print('b')
        I = self.data
        if(client.get('perceptual-memory') != None):
            print('c')
            #outMem = json.loads(client.get('perceptual-memory'))
            #outMem['I'] = I
            #client.set('perceptual-memory', json.dumps(outMem))
        else:
            print('d')
            #newMem = {'name': 'perceptual','ip/port': 'redis://redis:6379/','type': 'redis','I': I,'eval': 0.0}
            #client.set('perceptual-memory', json.dumps(newMem))
        
        self.request.sendall(self.data.upper())
        print((time.time_ns() - init))



        
 


def convert(string): 
    li = list(string.split(", ")) 
    return li 



if __name__ == "__main__":
    HOST, PORT = "perceptual", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
