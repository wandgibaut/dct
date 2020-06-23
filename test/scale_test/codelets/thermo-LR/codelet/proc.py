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
import dct

root_codelet_dir='/home/codelet'

def get_temperature(room, HOST, PORT):
	data = 'get_' + room + '_temperature'
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		# Connect to server and send data
		sock.connect((HOST, PORT))
		sock.sendall(bytes(data + "\n", "utf-8"))

		# Receive data from the server and shut down
		received = str(sock.recv(1024), "utf-8")
		return received
	#print('a')


def main(activation):
	temp = get_temperature('living-room', 'localhost', 9999)
	print(temp)
	I = float(temp)
	dct.setMemoryObjects(root_codelet_dir, 'perceptual-LR-thermo-LR-memory', 'I', str(I), 'outputs')
	#dct.setMemoryObjects(root_codelet_dir, 'energy-LR-thermo-LR-memory', 'I', str(I), 'outputs')
	dct.setMemoryObjects(root_codelet_dir, 'comfort-LR-thermo-LR-memory', 'I', str(I), 'outputs')






if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

