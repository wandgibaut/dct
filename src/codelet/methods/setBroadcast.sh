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

# usage: ./setBroadcast.sh <arg>
# where <arg> is a string with the broadcast to set
# example: ./setBroadcast.sh [{"name":....}, {"name":....}]

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setBroadcast.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list broadcast "$1"
fi
