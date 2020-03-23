import socketserver
import sys
import json

root_codelet_dir='/home/codelet'

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def getMemory(self, memory_name):
        with open(root_codelet_dir + '/' +memory_name + '.json', 'r+') as json_data:
            #return json.load(json_data)
            #print(json_data)
            memory = json.dumps(json.load(json_data))
            return memory


    def setMemory(self, memory_name, field, value):
        with open(root_codelet_dir + '/' +memory_name + '.json', 'r+') as json_data:
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
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        list_data = self.convert(self.data.decode())
        if(list_data[0] == 'get'):
            print(self.getMemory(list_data[1]))
            self.request.sendall(bytes(self.getMemory(list_data[1]), "utf-8"))
            #self.request.sendall(self.data)
            #self.request.sendall(bytes('{"name": "motor-memory", "ip/port": "172.28.1.1:9999", "type": "tcp", "I": null, "eval": 0.0}', "utf-8"))
        
        if(list_data[0] == 'set'):
            self.setMemory(list_data[1], list_data[2], list_data[3])
            self.request.sendall(bytes('success!', "utf-8"))
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    #HOST, PORT = "localhost", 9999
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

    