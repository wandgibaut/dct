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


# $1: codelet folder
# $2: ip:port of the container server
 
docker run -v $1/:/home --network host  --env root_codelet_dir=/home/codelet python_codelet /home/codelet/methods/run.sh $2 &
