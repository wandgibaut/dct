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

# Returns the codelet broadcast
# usage: ./getBroadcast.sh (optional) <arg1> <arg2>


if [ $# -eq 0 ]
then
    result= python3 $root_codelet_dir/methods/readField.py broadcast

elif [ $# -eq 1 ]
then
    result= python3 $root_codelet_dir/methods/readField.py broadcast $1

elif [ $# -eq 2 ]
then
    result= python3 $root_codelet_dir/methods/readField.py broadcast $1 $2

else
    echo "Wrong number of arguments!

usage: ./getBroadcast.sh (optional) <arg1> <arg2>"

fi


# use the following commands to retrieve and store the result: 
# result=$(./getBroadcast.sh)
# echo $result

