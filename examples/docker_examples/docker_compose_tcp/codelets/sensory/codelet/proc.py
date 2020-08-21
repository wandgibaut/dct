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
import json
import sys
import socket
import os
import dct

class SensoryCodelet(dct.PythonCodelet):

    def calculate_activation(self):
        print("new Activation")
        return 0.0

	def get_luminosity(room, HOST, PORT):
		data = 'get_' + room + '_luminosity'
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			# Connect to server and send data
			sock.connect((HOST, PORT))
			sock.sendall(bytes(data + "\n", "utf-8"))

			# Receive data from the server and shut down
			received = str(sock.recv(1024), "utf-8")
			return received
		#print('a')

    def proc(self, activation):
        temp = get_luminosity('living-room', 'localhost', 9999)
		#print(temp)
		I = float(temp)
		dct.setMemoryObjects(root_codelet_dir, 'perceptual-LR-luminosity-LR-memory', 'I', str(I), 'outputs')
		dct.setMemoryObjects(root_codelet_dir, 'energy-LR-luminosity-LR-memory', 'I', str(I), 'outputs')
		dct.setMemoryObjects(root_codelet_dir, 'comfort-LR-luminosity-LR-memory', 'I', str(I), 'outputs')



if __name__ == '__main__':
    print(os.getenv('ROOT_CODELET_DIR'))
    codelet = TestCodelet(name='defaultCodelet')
    codelet.run()