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
import time
import subprocess
import dct # the dct utility module
import redis
from pymongo import MongoClient

root_codelet_dir= os.getenv('root_codelet_dir')

def calculate_activation():
	########################################
    ## Write you code below! ##
    print("default activation")
    return 0
    ## End of main code! ## 
    ########################################



def main(activation):
    ########################################
    ## Write you code below! ##
    print("default Codelet")
    
    ## End of main code! ## 
    ########################################



if __name__ == '__main__':
    timestep = float(subprocess.check_output(["python3", root_codelet_dir + "/methods/readField.py", "timestep"]))
    print(timestep)
    loop = subprocess.check_output(["python3", root_codelet_dir + "/methods/readField.py", "loop"])
    while loop:
        activation = calculate_activation()
        main(activation)
        loop = subprocess.check_output(["python3", root_codelet_dir + "/methods/readField.py", "loop"])
        time.sleep(timestep)
    sys.exit()

