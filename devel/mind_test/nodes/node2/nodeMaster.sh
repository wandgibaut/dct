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

# initialize any number of servers, usually just one
if [ $# -ne 0 ]
    then
        echo "initiating servers!"
        for var in "$@"
        do
            python3 $ROOT_NODE_DIR/server.py "$var"  &
        done
fi

# run all codelet that should run
mapfile -t <$ROOT_NODE_DIR/init_codelets.txt

for var in "${MAPFILE[@]}"
do
  python3 $ROOT_NODE_DIR/codelets/$var/codelet.py  &
done

# periodically check the health
# TODO: implement caring routines
while true
do
  sleep 1
done

