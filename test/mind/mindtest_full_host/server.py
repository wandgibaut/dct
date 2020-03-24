import socketserver

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
            return json.load(json_data)


    def setMemory(self, memory_name, field, value):
        with open(root_codelet_dir + '/' +memory_name + '.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData['field'] = value
            json_data.seek(0) #rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

                                            

    def convert(self, string): 
        li = list(string.split("/")) 
        return li 

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        list_data = self.convert(data)
        if(list_data[0] == 'get'):
            self.request.sendall(getMemory(list_data[1]))
        
        if(list_data[0] == 'set'):
            getMemory(list_data[1], list_data[2], list_data[3])
            self.request.sendall('success!')
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    #HOST, PORT = "localhost", 9999
    args = sys.argv[1:]
    if len(args) == 2:
        HOST= args[0]
        PORT  = args[1]
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    else:
        print(len(args))
        print('Error! Wrong number of arguments!')
        sys.exit()

    