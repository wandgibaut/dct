#!/bin/bash

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

# Returns if he codelet is looping
# usage: ./getLoop.sh


result= python3 $root_codelet_dir/methods/readField.py loop

# use the following commands to retrieve and store the result: 
# result=$(./getLoop.sh)
# echo $result
