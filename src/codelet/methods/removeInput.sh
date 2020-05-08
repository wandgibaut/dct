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

# usage: ./removeInput.sh <field> <value>
# example: ./removeInput.sh ip/port 127.0.0.1:6000


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./removeInput.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py remove inputs $1
fi
