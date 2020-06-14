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

# Returns the codelet outputs
# usage: ./getOutput.sh (optional) <arg1> <arg2>


if [ $# -eq 0 ]
then
    result= python3 $root_codelet_dir/methods/readField.py outputs

elif [ $# -eq 1 ]
then
    result= python3 $root_codelet_dir/methods/readField.py outputs $1

elif [ $# -eq 2 ]
then
    result= python3 $root_codelet_dir/methods/readField.py outputs $1 $2

else
    echo "Wrong number of arguments!

usage: ./getOutput.sh (optional) <arg1> <arg2>"

fi


# use the following commands to retrieve and store the result: 
# result=$(./getOutputs.sh)
# echo $result

#list of all
# name
# name index
