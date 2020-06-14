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

# usage: ./setBroadcast.sh <arg>
# where <arg> is a string with the broadcast to set
# example: ./setBroadcast.sh [{"name":....}, {"name":....}]


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setBroadcast.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list broadcast "$1"
fi
