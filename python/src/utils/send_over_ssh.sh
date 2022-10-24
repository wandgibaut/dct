#!/bin/bash

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


# $1: codelet to pass 
# $3: user@ipaddress
# $3: /path/to/destination
# $4: root_codelet_dir


#send the files
scp -r $1 $2:$3

#set environment variable 
ssh $2 "echo $4 >> ~/.bashrc"
