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
import time
root_codelet_dir='/home/codelet'


def set_ac(room, HOST, PORT,temp):
	data = 'set_' + room + '_AC_[true,' + temp +']'
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((HOST, PORT))
		sock.sendall(bytes(data + "\n", "utf-8"))
		# Receive data from the server and shut down
		received = str(sock.recv(1024), "utf-8")
		return received

def reset_ac(room, HOST, PORT):
	data = 'set_' + room + '_AC_false'
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((HOST, PORT))
		sock.sendall(bytes(data + "\n", "utf-8"))
		# Receive data from the server and shut down
		received = str(sock.recv(1024), "utf-8")
		return received


def main(activation):
    # print(socket.gethostbyname(socket.gethostname()))
	mem = dct.getMemoryObjects(root_codelet_dir, 'AC-relay-LR-AC-control-LR-memory', 'inputs')
	I = mem['I']
	print(I)
	if I != 'off':
		set_ac('living-room', 'localhost', 9999, I)
		time.sleep(.2)
	else:
		reset_ac('living-room', 'localhost', 9999)
		time.sleep(.2)

	print(I)
    



if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

