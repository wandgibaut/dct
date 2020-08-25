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

check_integrity()
{
  for PID in "${PIDARRAY[@]}"
  do
    if [[ -d "/proc/${PID}" ]]
    then
      echo "process ${PID} exists"
    else
      regenerate_process "$PID"
    fi
  done
}

regenerate_process()
{
  for i in "${!PIDARRAY[@]}"; do
    if [[ "${PIDARRAY[$i]}" = "$1" ]]; then
      if [[ "${NAMEARRAY["$i"]}"  = "server" ]]; then
        python3 "$ROOT_NODE_DIR"/server.py "$var"  &
        PIDARRAY["$i"]=$!
      else
        python3 "$ROOT_NODE_DIR"/codelets/"${NAMEARRAY["$i"]}"/codelet.py  &
        PIDARRAY["$i"]=$!
        echo "regenerated ${NAMEARRAY[$i]}"
      fi
    fi
  done
}

# array to index all pids
PIDARRAY=()
NAMEARRAY=()
# initialize any number of servers, usually just one
if [ $# -ne 0 ]
    then
        echo "initiating servers!"
        for var in "$@"
        do
            NAMEARRAY+=("server")
            python3 "$ROOT_NODE_DIR"/server.py "$var"  &
            PIDARRAY+=($!)
        done
fi

# run all codelet that should run
mapfile -t <"$ROOT_NODE_DIR"/init_codelets.txt

for var in "${MAPFILE[@]}"
do
  NAMEARRAY+=("$var")
  python3 "$ROOT_NODE_DIR"/codelets/"$var"/codelet.py  &
  PIDARRAY+=($!)
done

# periodically check the health
# TODO: implement caring routines
while true
do
  check_integrity
  sleep 10 #check every 10 secs
done

