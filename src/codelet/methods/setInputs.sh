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

# usage: ./setInputs.sh <arg>
# where <arg> is a string with the inputs to set
# example: ./setInputs.sh [{"name":....}, {"name":....}]


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setInputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list inputs "$1"
fi
