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

# usage: ./setActivation.sh <arg>
# where <arg> is the activation to set
# example: ./setActivation.sh 0.5

# TODO: check boundaries


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setActivation.sh <arg>"
    else
        python3 $root_codelet_dir/methods?changeField.py activation $1
fi
