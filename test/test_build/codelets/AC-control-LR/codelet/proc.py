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
min_temp = 12

def main(activation):
	mem = dct.getMemoryObjects(root_codelet_dir, 'AC-control-LR-perceptual-LR-memory', 'inputs')
	mem_2 = dct.getMemoryObjects(root_codelet_dir, 'AC-control-LR-comfort-LR-memory', 'inputs')
	mem_3 = dct.getMemoryObjects(root_codelet_dir, 'AC-control-LR-energy-LR-memory', 'inputs')
	#print(mem_2['I'])
	
	if float(mem_3['I']) == 0.0:
		# if there is someone, aplly normal rule
		if float(mem_2['I']) != 0:
			I = min_temp + 12*(1- float(mem_2['I']))
		else:
			I = 'off'
	else:
		I = 'off'
	#if hasahss send null
	#else send AC temp
	#print(I)
	dct.setMemoryObjects(root_codelet_dir, 'AC-relay-LR-AC-control-LR-memory', 'I', str(I), 'outputs')




if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

