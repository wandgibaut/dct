#!/bin/bash

# usage: ./setBroadcast.sh <arg>
# where <arg> is a string with the broadcast to set
# example: ./setBroadcast.sh [{"name":....}, {"name":....}]

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setBroadcast.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list broadcast "$1"
fi
