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
import sys
import dct
import json
import subprocess

def create_connections_file():
    print('a')

def main(codelet_folder, ip_port_host, port_to_expose, source_codelets):
    with open(codelet_folder + '/codelet/fields.json', 'r+') as json_data:
        codelet_info = json.load(json_data)

        # add all source codelets outputs as the new codelet inputs
        for source_codelet in source_codelets:
            ip_port = convert(":", source_codelet)
            source_codelet_info = dct.getCodeletInfo(ip_port[0], ip_port[1])
            new_inputs = []
            new_inputs[:] = [mem for mem in source_codelet_info['outputs'] if  mem not in codelet_info['inputs']] 
            codelet_info['inputs'].extend(new_inputs)
            #codelet_info['inputs'].extend(source_codelet_info['outputs'])

        # updates the fields.json
        json_data.seek(0) #rewind
        json.dump(codelet_info, json_data)
        json_data.truncate()

        print(codelet_folder + ' ' + ip_port_host  + ' ' + port_to_expose)
        # calls the add simple container script
        subprocess.check_call(['./add_simple_container.sh', codelet_folder, ip_port_host, port_to_expose])
    
    

def convert(separator, string): 
    li = list(string.split(separator)) 
    return li 


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 3:
        #print(args)
        main(args[0], args[1], args[2], args[3:])
	
    else:
        print(len(args))
        print('Error! Wrong number of arguments!')
        sys.exit()
