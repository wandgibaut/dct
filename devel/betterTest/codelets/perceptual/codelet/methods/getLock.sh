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

# Returns if the codelet is locked
# usage: ./getLock.sh


result= python3 $root_codelet_dir/methods/readField.py lock
# use the following commands to retrieve and store the result: 
# result=$(./getLock.sh)
# echo $result
