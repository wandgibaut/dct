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
	#mem = dct.getMemoryObjects(root_codelet_dir, 'perceptual-LR-thermo-LR-memory', 'inputs')
	#mem_2 = dct.getMemoryObjects(root_codelet_dir, 'perceptual-LR-luminosity-LR-memory', 'inputs')
	#mem_3 = dct.getMemoryObjects(root_codelet_dir, 'perceptual-LR-presence-LR-memory', 'inputs')
	all_mem = dct.getMemoryObjectsGroup(root_codelet_dir, 'inputs', 'sensors')
	
	I = ''
	for mem in all_mem:
		if I == '':
			I = mem['I']
		else:
			I = I + '-' + mem['I']

	print(I)
	
	dct.setMemoryObjects(root_codelet_dir, 'AC-control-LR-perceptual-LR-memory', 'I', I, 'outputs')
	dct.setMemoryObjects(root_codelet_dir, 'light-control-LR-perceptual-LR-memory', 'I', I, 'outputs')

    
 


if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

