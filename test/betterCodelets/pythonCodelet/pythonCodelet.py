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

#root_codelet_dir= os.getenv('root_codelet_dir')

class pythonCodelet:
    def __init__(self, name=None, root_codelet_dir=os.getenv('root_codelet_dir')):
        self.root_codelet_dir = root_codelet_dir
        self.name = name

    #TODO: getters and setters
    def check_field(self, field):
        return subprocess.check_output(["python3", self.root_codelet_dir + "/methods/readField.py", field])


    def run(self):
        while(bool(self.check_field('enable'))):
            while(not bool(self.check_field('lock'))):
                activation = self.calculate_activation()
                self.proc(activation)
                time.sleep(float(self.check_field('timestep')))

        sys.exit()


    def calculate_activation(self):
        ########################################
        ## Write you code below! ##
        print("default activation")
        return 0
        ## End of main code! ## 
        ########################################



    def proc(self, activation):
        ########################################
        ## Write you code below! ##
        print("default proc")
        
        ## End of main code! ## 
        ########################################



if __name__ == '__main__':
    codelet = pythonCodelet(name='defaultCodelet')
    codelet.run()
        

