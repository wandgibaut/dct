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

target_temperature = 15
target_luminosity = 1.0

def bound_value(value):
	if value > 1.0:
		value = 1.0
	elif value < 0.0:
		value = 0.0
	return value

def main(activation):
	mem = dct.getMemoryObjects(root_codelet_dir, 'comfort-LR-thermo-LR-memory', 'inputs')
	mem_2 = dct.getMemoryObjects(root_codelet_dir, 'comfort-LR-luminosity-LR-memory', 'inputs')
	#mem_3 = dct.getMemoryObjects(root_codelet_dir, 'comfort-LR-presence-LR-memory', 'inputs')
	#TODO: make a correct formula
	#print(mem['I'])
	#I = bound_value((float(mem['I']) - target_temperature +2)/10)
	if float(mem['I']) > (target_temperature +1):
		I = 1.0
		dct.setMemoryObjects(root_codelet_dir, 'AC-control-LR-comfort-LR-memory', 'I', str(I), 'outputs')
	elif float(mem['I']) < (target_temperature -1):
		I = 0.0
		#print(I)
		dct.setMemoryObjects(root_codelet_dir, 'AC-control-LR-comfort-LR-memory', 'I', str(I), 'outputs')
	else:
		I = 'dont_care'
		#dct.setMemoryObjects(root_codelet_dir, 'AC-control-LR-comfort-LR-memory', 'I', str(I), 'outputs')#'dont_care'
	
	if float(mem_2['I']) < (target_luminosity):
		I_2 = 1.0
		dct.setMemoryObjects(root_codelet_dir, 'light-control-LR-comfort-LR-memory', 'I', str(I_2), 'outputs')
	else:
		I_2 = 0.0
		dct.setMemoryObjects(root_codelet_dir, 'light-control-LR-comfort-LR-memory', 'I', str(I_2), 'outputs')
	
	

    
 


if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

