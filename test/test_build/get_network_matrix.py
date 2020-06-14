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

import socket
import json
import sys
import networkx as nx
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# com base em uma lista de ip/port
# de um info pra cada server
# veja lista de codelets

def getCodeletInfo(host, port):
    data = 'info_'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,int(port)))
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

def getAllCodeletsInfos(list_of_codelets):
    answer = []
    for codelet in list_of_codelets:
        print(codelet)
        answer.append(getCodeletInfo(codelet[0], codelet[1]))
    
    return answer

def createMatrix(list_of_codelets_infos):
    #empty matrix
    matrix=[]
    for i in range(len(list_of_codelets_infos)): 
        row=[]
        for j in range(len(list_of_codelets_infos)): 
            row.append(0)
        matrix.append(row)

    # fill matrix
    for i in range(len(list_of_codelets_infos)):
        codelet_i = list_of_codelets_infos[i]
        inputs_i = codelet_i['inputs']
        outputs_i = codelet_i['outputs']
        for j in range(len(list_of_codelets_infos)):
            for k in range(len(inputs_i)):
                if inputs_i[k] in list_of_codelets_infos[j]['outputs']:
                    matrix[i][j] = 1
            
            for k in range(len(outputs_i)):
                if outputs_i[k] in list_of_codelets_infos[j]['inputs']:
                    matrix[i][j] = 1
            
            # se inputs == outputs, marque uma conexão

    return matrix
    
def drawNetwork(matrix):
    print(matrix)
    g = nx.from_numpy_matrix(np.array(matrix)) 
    f = plt.figure()
    nx.draw(g, ax=f.add_subplot(111), with_labels=True)
    f.savefig("graph.png")


def convert(separator, string): 
    li = list(string.split(separator)) 
    return li 

def main(args):
    list_of_codelets = []
    for ip in args:
        list_of_codelets.append(convert(":",ip))

    matrix = createMatrix(getAllCodeletsInfos(list_of_codelets))
    drawNetwork(matrix)
    

if __name__ == '__main__':
    args = sys.argv[1:]
        
    main(args)
