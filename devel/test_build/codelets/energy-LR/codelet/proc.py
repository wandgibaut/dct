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

import json
import sys
import redis
from pymongo import MongoClient
import socket
import dct

root_codelet_dir='/home/codelet'


def main(activation):
	#mem = dct.getMemoryObjects(root_codelet_dir, 'energy-LR-thermo-LR-memory', 'inputs')
	#mem_2 = dct.getMemoryObjects(root_codelet_dir, 'energy-LR-luminosity-LR-memory', 'inputs')
	mem_3 = dct.getMemoryObjects(root_codelet_dir, 'energy-LR-presence-LR-memory', 'inputs')
	
	I = 1- float(mem_3['I'])

	dct.setMemoryObjects(root_codelet_dir, 'AC-control-LR-energy-LR-memory', 'I', str(I), 'outputs')
	dct.setMemoryObjects(root_codelet_dir, 'light-control-LR-energy-LR-memory', 'I', str(I), 'outputs')

    
 


if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

