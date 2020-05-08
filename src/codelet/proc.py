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
import os
import dct # the dct utility module

root_codelet_dir= os.getenv('root_codelet_dir')

def main(activation):
    ########################################
    ## Write you code below! ##
    print("default Codelet")
    
    ## End of main code! ## 
    ########################################



if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

