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

# usage: call your program or write directly here
# remember $1 is the activation and $2 is a json object with memories 

############# write your program bellow ##############

root_codelet_dir=/home/codelet

python $root_codelet_dir/proc.py $1 #$2

