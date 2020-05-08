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

# usage: ./addOutput.sh <arg>
# where <arg> is a string with the outputs to set
# example: ./addOutput.sh '{"key": "value"}'


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setOutputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py add outputs "$1"
fi


# must format like this: '{"key": "value"}' when called
