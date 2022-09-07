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


# $1: node folder
# $2: ip:port of the container server
# $3: container name 

docker run --name $3 -d -it --network host  --env ROOT_NODE_DIR=/home/node wandgibaut/python_codelet /bin/bash &
sleep 2
docker cp $1/. $3:/home/node
docker exec -d $3 /home/node/nodeMaster.sh $2 &
