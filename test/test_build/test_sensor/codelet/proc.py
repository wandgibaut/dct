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
#import redis
#from pymongo import MongoClient
import socket
import dct
import math
import time

root_codelet_dir='/home/codelet'
steps= 1000




def main(activation):
	mem = {"name": "sin-memory", 
	"ip/port": "localhost:9998", 
	"type": "tcp", 
	"group": ["sensors"], 
	"I": "24.0", 
	"eval": 0.0}
	

	for i in range(steps):
		mem['I'] = math.sin(i*(2*math.pi/steps))
		print(dct.getMemoryObjects(root_codelet_dir, 'perceptual-LR-input-container-memory', 'outputs'))
		
		dct.setMemoryObjects(root_codelet_dir, 'perceptual-LR-input-container-memory', 'sin-memory', json.dumps(mem), 'outputs')
		time.sleep(.5)
    



if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

