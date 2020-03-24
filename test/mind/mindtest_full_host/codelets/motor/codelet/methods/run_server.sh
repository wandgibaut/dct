#!/bin/bash

root_codelet_dir=/home/codelet

run=$($root_codelet_dir/methods/getLoop.sh)

if [ $# -eq 2 ]
    then
        echo "initiating server!"
        python3 $root_codelet_dir/server.py "$1" "$2"
    else
        echo "error initializing server!"
fi
