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

import json
from pymongo import MongoClient
import redis


def mount(list_of_codelets):
    for codelet in list_of_codelets:
        with open('/home/codelets/'+ codelet + '/codelet/fields.json', 'r+') as json_data:  # abrir o fields
            jsonData = json.load(json_data)
            inputs = jsonData['inputs']
            outputs = jsonData['outputs']
            codelet_name = jsonData['name']
            
            for inputMemory in inputs:
                try:
                    if inputMemory['type'] == 'mongo':
                        client = MongoClient(inputMemory['ip/port']) # METODO: vai no ip
                        base = client['database-raw-memory']
                        inMem = base[convert(inputMemory['name'])[0]] # define base, collection (input name)
                        mem = inMem.find_one(
                            {'name': convert(inputMemory['name'])[1]}) # e checa se existe uma memoria com esse name

                        if(mem == None):  # se sim, deixa quieto, se não, cria
                            memory = {'name': convert(inputMemory['name'])[1],'ip/port': inputMemory['ip/port'],'type': 'mongo','I': None,'eval': 0.0}
                            inMem.insert_one(memory)
                            print(memory)
                        
                    if inputMemory['type'] == 'redis':
                        client = redis.Redis(host=convert_alt(inputMemory['ip/port'])[0], port=convert(convert_alt(inputMemory['ip/port'])[2])[0])
                        
                        mem = {'name': convert(inputMemory['name'])[1],'ip/port': inputMemory['ip/port'],'type': 'redis','I': None,'eval': 0.0}
                        client.set(convert(inputMemory['name'])[1], json.dumps(mem))
                    
                    if inputMemory['type'] == 'tcp':
                        print('tcp')
                except: 
                    print('an error has occurred!!')
       


def convert(string): 
    li = list(string.split("/")) 
    return li 

def convert_alt(string): 
    li = list(string.split(":")) 
    return li 


if __name__ == '__main__':
    list_of_codelets = ['sensory', 'perceptual', 'behavioral', 'motor']
    mount(list_of_codelets)
	
    # TODO: read all codelets in codelets programatically

