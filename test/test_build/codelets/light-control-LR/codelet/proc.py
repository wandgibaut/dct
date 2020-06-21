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
import redis
from pymongo import MongoClient
import socket
import dct

root_codelet_dir='/home/codelet'


def main(activation):
	mem = dct.getMemoryObjects(root_codelet_dir, 'light-control-LR-comfort-LR-memory', 'inputs')
	mem_2 = dct.getMemoryObjects(root_codelet_dir, 'light-control-LR-energy-LR-memory', 'inputs')
	mem_3 = dct.getMemoryObjects(root_codelet_dir, 'light-control-LR-perceptual-LR-memory', 'inputs')
	
	if float(mem_2['I']) == 0.0:
	# if there is someone, turn the lights on
		I = 1.0	
	else:
		I = 0.0

	dct.setMemoryObjects(root_codelet_dir, 'light-switchs-LR-light-control-LR-memory', 'I', str(I), 'outputs')




if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

