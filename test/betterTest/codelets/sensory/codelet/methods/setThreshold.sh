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

# usage: ./setThreshold.sh <arg>
# where <arg> is the threshold to set
# example: ./setThreshold.sh 0.5

# TODO: check boundaries


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setThreshold.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py threshold $1
fi

