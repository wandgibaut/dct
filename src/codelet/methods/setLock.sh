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

# usage: ./setLock.sh <arg>
# where <arg> is true or false
# example: ./setLock.sh true


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setLock.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py lock $1
fi
