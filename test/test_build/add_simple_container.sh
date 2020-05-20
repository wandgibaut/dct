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


# $1: codelet folder
# $2: ip:port of the container server
 
#docker run -v $1/:/home --network host  --env root_codelet_dir=/home/codelet python_codelet /home/codelet/methods/run.sh $2 &

#docker create --name $3 --env root_codelet_dir=/home/codelet python_codelet
#docker cp $1 $3:/home
#docker start $3
#docker exec -d $3 /home/codelet/methods/run.sh $2 &

docker run --name $3 -d -it --network host  --env root_codelet_dir=/home/codelet python_codelet /bin/bash &
sleep 1
docker cp $1/. $3:/home
docker exec -d $3 /home/codelet/methods/run.sh $2 &
