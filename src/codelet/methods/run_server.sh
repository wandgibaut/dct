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


run=$($root_codelet_dir/methods/getLoop.sh)

if [ $# -eq 2 ]
    then
        echo "initiating server!"
        python3 $root_codelet_dir/server.py "$1" "$2"
    else
        echo "error initializing server!"
fi
