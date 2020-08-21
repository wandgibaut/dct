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
import sys
import dct
import json
import subprocess
import random
import socket
import numpy as np

def add_codelet_to_system(codelet_folder, ip_port_hostmode, source_codelets_ips):
    with open(codelet_folder + '/codelet/fields.json', 'r+') as json_data:
        codelet_info = json.load(json_data)

        # add all source codelets outputs as the new codelet inputs
        for source_codelet in source_codelets_ips:
            ip_port = convert(":", source_codelet)
            print(source_codelets_ips)
            print(ip_port)
            source_codelet_info = dct.getCodeletInfo(ip_port[0], ip_port[1])
            new_inputs = []
            new_inputs[:] = [mem for mem in source_codelet_info['outputs'] if  mem not in codelet_info['inputs']] 
            codelet_info['inputs'] = new_inputs
            #codelet_info['inputs'].extend(new_inputs)
            #codelet_info['inputs'].extend(source_codelet_info['outputs'])

        # updates the fields.json
        json_data.seek(0) #rewind
        json.dump(codelet_info, json_data)
        json_data.truncate()

        print(codelet_folder + ' ' + ip_port_hostmode)
        # calls the add simple container script
        subprocess.check_call(['./add_simple_container.sh', codelet_folder, ip_port_hostmode, 'test_' + str(random.randint(0,1000))])
    


def add_random_consumer(codelet_folder, ip_port_hostmode, number_of_feeders, list_of_codelets_json):
    with open(list_of_codelets_json, 'r+') as json_data:
        codelets_info = json.load(json_data)
        ips= list(map(lambda datum: datum['ip/port'], codelets_info))
        
        source_codelets_ips = []
        if number_of_feeders == '-1':
            source_codelets_ips.extend(random.choices(ips, k=random.randrange(len(codelets_info))))
        else:
            source_codelets_ips.extend(random.choices(ips, k=int(number_of_feeders)))
        
        print(source_codelets_ips)
        add_codelet_to_system(codelet_folder, ip_port_hostmode, source_codelets_ips)


def add_multiple_random_consumers(codelet_folder, ip_port_hostmode_list_json, number_of_feeders_array, list_of_codelets_json, number_of_codelets):
    with open(ip_port_hostmode_list_json, 'r+') as json_list:
        ip_port_hostmode_list = json.load(json_list)
        if number_of_feeders_array == '-1':
            for i in range(number_of_codelets):
                with open(list_of_codelets_json, 'r+') as json_data:
                    codelets_info = json.load(json_data)
                    for i in range(int(number_of_codelets)):
                        add_random_consumer(codelet_folder, ip_port_hostmode_list[i], -1, codelets_info)
        else:
            for i in range(number_of_codelets):
                for i in range(int(number_of_codelets)):
                    add_random_consumer(codelet_folder, ip_port_hostmode_list[i], number_of_feeders_array[i], list_of_codelets_json)


def add_multiple_scale_consumers(codelet_folder, list_of_codelets_json, number_of_codelets, ip_port_hostmode_list_json):
    with open(ip_port_hostmode_list_json, 'r+') as json_list:
        ip_port_hostmode_list = json.load(json_list)
        
        with open(list_of_codelets_json, 'r+') as json_data:
            codelets_info = json.load(json_data)
            ips= list(map(lambda datum: datum['ip/port'], codelets_info))
            list_of_codelets = []
            for ip in ips:
                list_of_codelets.append(convert(":",ip))
            matrix = np.array(createMatrix(getAllCodeletsInfos(list_of_codelets)))
            number_of_connections = matrix.sum(axis=1,dtype='float')
            total_number_of_connections = matrix.sum(dtype='float')
            #print(number_of_connections)
            #print(total_number_of_connections)
            density = number_of_connections/total_number_of_connections
            #print(density)
            #new_total_number_of_connections = total_number_of_connections + int(number_of_codelets)

            #new_number_of_connections = np.round(density*new_total_number_of_connections)
            #print(new_number_of_connections)
            #print(np.sort(new_number_of_connections)[::-1])
            draw = np.random.choice(ips,10,p=density)
            print(draw)

            for i in range(int(number_of_codelets)):
                #print(ip_port_hostmode_list[i])
                source_codelets = [draw[i]]
                #source_codelets.append(draw[i])
                #print('here is your array: ')
                #print(source_codelets)
                add_codelet_to_system(codelet_folder, ip_port_hostmode_list[i],source_codelets)
                #print (i)

        #TODO: continuar

def remove_docker_codelet_from_system(codelet_name):
    # calls the add simple container script
    subprocess.check_call(['docker stop', codelet_name])



def getCodeletInfo(host, port):
    data = 'info_'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host,int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        #print(received)
        try:
            answer = json.loads(received)
        except:
            answer = []
            raise Exception
        return answer

def getAllCodeletsInfos(list_of_codelets):
    answer = []
    for codelet in list_of_codelets:
        #print(codelet)
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

def convert(separator, string): 
    li = list(string.split(separator)) 
    return li 


if __name__ == '__main__':
    args = sys.argv[1:]
    
    if args[0] == 'random':
        if len(args) > 4:
            add_random_consumer(args[1], args[2], args[3], args[4])
        else:
            print('Error! Wrong number of arguments!')
    elif args[0] == 'specific':
        if len(args) > 3:
            add_codelet_to_system(args[1], args[2], args[3:])
        else:
            print('Error! Wrong number of arguments!')
    elif args[0] == 'scale':
        add_multiple_scale_consumers(args[1], args[2], args[3], args[4])
    else:
        print(len(args))
        print('Error! Wrong number of arguments!')
        sys.exit()
