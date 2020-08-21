# *****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the MIT License                       #
# which accompanies this distribution, and is available at                    #
# https://opensource.org/licenses/MIT                                         #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
# *****************************************************************************#
import sys
import getopt
import dct
import json
import subprocess
import random
import socket
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def add_codelet_to_system(codelet_folder, ip_port_hostmode, new_codelet_name, input_codelets_ips=None,
                          input_memories=None, output_codelets_ips=None, output_memories=None):
    with open(codelet_folder + '/codelet/fields.json', 'r+') as json_data:
        codelet_info = json.load(json_data)

        print('test stops here')
        # add all source codelets outputs as the new codelet inputs
        if input_codelets_ips is not None:
            new_inputs = []
            for input_codelet in input_codelets_ips:
                ip_port = convert(":", input_codelet)
                print(input_codelets_ips)
                input_codelet_info = dct.get_codelet_info(ip_port[0], ip_port[1])

                for mem in input_codelet_info['outputs']:
                    if mem not in codelet_info['inputs'] and mem['name'] in input_memories:
                        new_inputs.append(mem)

            codelet_info['inputs'] = new_inputs

        # add all output codelets outputs as the new codelet inputs
        if output_codelets_ips is not None:
            new_outputs = []
            for output_codelet in output_codelets_ips:
                ip_port = convert(":", output_codelet)
                print(output_codelets_ips)
                output_codelet_info = dct.get_codelet_info(ip_port[0], ip_port[1])

                for mem in output_codelet_info['outputs']:
                    if mem not in codelet_info['inputs'] and mem['name'] in output_memories:
                        new_outputs.append(mem)

            codelet_info['outputs'] = new_outputs

        # updates the fields.json
        json_data.seek(0)  # rewind
        json.dump(codelet_info, json_data)
        json_data.truncate()

        print(codelet_folder + ' ' + ip_port_hostmode)
        # calls the add simple container script
        subprocess.check_call(['./add_simple_container.sh', codelet_folder, ip_port_hostmode, new_codelet_name])


def add_random_consumer(codelet_folder, ip_port_hostmode, number_of_feeders, list_of_codelets_json):
    with open(list_of_codelets_json, 'r+') as json_data:
        codelets_info = json.load(json_data)
        ips= list(map(lambda datum: datum['ip/port'], codelets_info))
        
        input_codelets_ips = []
        input_memories = []
        if number_of_feeders == '-1':
            input_codelets_ips.extend(random.choices(ips, k=random.randrange(len(codelets_info))))
        else:
            input_codelets_ips.extend(random.choices(ips, k=int(number_of_feeders)))

        for ip in input_codelets_ips:
            ip_port = convert(":", ip)
            input_memories.extend(dct.get_codelet_info(ip_port[0], ip_port[1]))
        
        print(input_codelets_ips)
        add_codelet_to_system(codelet_folder, ip_port_hostmode, 'random_' + str(random.randint(0,1000)),
                              input_codelets_ips=input_codelets_ips, input_memories=input_memories)


def add_multiple_random_consumers(codelet_folder, ip_port_hostmode_list_json, number_of_feeders_array,
                                  list_of_codelets_json, number_of_codelets):
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
                    add_random_consumer(codelet_folder, ip_port_hostmode_list[i], number_of_feeders_array[i],
                                        list_of_codelets_json)


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
            number_of_connections = matrix.sum(axis=1, dtype='float')
            total_number_of_connections = matrix.sum(dtype='float')

            density = number_of_connections/total_number_of_connections

            draw = np.random.choice(ips, 10, p=density)
            print(draw)

            for i in range(int(number_of_codelets)):
                input_codelets_ips = [draw[i]]
                input_memories = []
                for ip in input_codelets_ips:
                    ip_port = convert(":", ip)
                    input_memories.extend(dct.get_codelet_info(ip_port[0], ip_port[1]))
                add_codelet_to_system(codelet_folder, ip_port_hostmode_list[i],input_codelets_ips=input_codelets_ips,
                                      input_memories=input_memories)

        #TODO: continuar


def remove_docker_codelet_from_system(codelet_name):
    # calls the add simple container script
    subprocess.check_call(['docker stop', codelet_name])


def get_codelet_info(host, port):
    data = 'info_'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, int(port)))
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        try:
            answer = json.loads(received)
        except:
            answer = []
            raise Exception
        return answer


def get_all_codelets_infos(list_of_codelets):
    answer = []
    for codelet in list_of_codelets:
        answer.append(getCodeletInfo(codelet[0], codelet[1]))
    
    return answer


def create_matrix(list_of_codelets_infos):
    # empty matrix
    matrix = []
    for i in range(len(list_of_codelets_infos)): 
        row = []
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


def draw_network(list_of_codelets, graph_name):
    matrix = createMatrix(getAllCodeletsInfos(list_of_codelets))

    print(matrix)
    g = nx.from_numpy_matrix(np.array(matrix))
    f = plt.figure()
    nx.draw(g, ax=f.add_subplot(111), with_labels=True)
    f.savefig(graph_name)


def convert(separator, string): 
    li = list(string.split(separator)) 
    return li 


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:f:e:c:i:m:O:M:s:l:L:n:C:", ["help=", "option=", "codelet-folder=",
                                                                                 "ip-port=", "codelet-name=",
                                                                                 "input-ips=", "input-memories=",
                                                                                 "output-ips=",
                                                                                 "output-memories=", "sources=",
                                                                                 "ip-port-hostmode-list-json=",
                                                                                 "list-of-codelets-json=",
                                                                                 "number-of-codelets=",
                                                                                 "list-of-codelets="])
    except getopt.GetoptError:
        print('devel')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('help')
            sys.exit()
        elif opt in ('-o', '--option'):
            option = arg
        elif opt in ('-f', '--codelet-folder'):
            codelet_folder = arg
        elif opt in ('-e', '--ip-port'):
            ip_port_hostmode = arg
        elif opt in ('-c', '--codelet-name'):
            new_codelet_name = arg
            codelet_name = arg
        elif opt in ('-i', '--input-ips'):
            input_codelets_ips = arg.split(',')
        elif opt in ('-m', '--input-memories'):
            input_memories = arg.split(',')
        elif opt in ('-O', '--output-ips'):
            output_codelets_ips = arg.split(',')
        elif opt in ('-M', '--output-memories'):
            output_memories = arg.split(',')
        elif opt in ('-s', '--sources'):
            number_of_feeders_array = arg.split(',')
            if len(number_of_feeders_array) == 1:
                number_of_feeders = number_of_feeders_array[0]
        elif opt in ('-l', '--ip-port-hostmode-list-json'):
            ip_port_hostmode_list_json = arg
        elif opt in ('-L', '--list-of-codelets-json'):
            list_of_codelets_json = arg
        elif opt in ('-n', '--number-of-codelets'):
            number_of_codelets = arg
        elif opt in ('-C', 'list-of-codelets'):
            list_of_codelets = arg.split(',')

    try:
        if option == 'random':
            add_random_consumer(codelet_folder, ip_port_hostmode, number_of_feeders, list_of_codelets_json)

        elif option == 'consumer':
            add_codelet_to_system(codelet_folder, ip_port_hostmode, new_codelet_name,
                                  input_codelets_ips=input_codelets_ips, input_memories=input_memories)

        elif option == 'scale':
            add_multiple_scale_consumers(codelet_folder, list_of_codelets_json, number_of_codelets,
                                         ip_port_hostmode_list_json)

        elif option == 'multiple-random':
            add_multiple_random_consumers(codelet_folder, ip_port_hostmode_list_json, number_of_feeders_array,
                                          list_of_codelets_json, number_of_codelets)

        elif option == 'remove':
            remove_docker_codelet_from_system(codelet_name)

        elif option == 'draw-network':
            draw_network(list_of_codelets, "graph.png")
    except:
        print('Error!')

    sys.exit()
