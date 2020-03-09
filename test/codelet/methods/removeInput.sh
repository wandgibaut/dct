#!/bin/bash

# usage: ./removeInput.sh <field> <value>
# example: ./removeInput.sh ip/port 127.0.0.1:6000

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./removeInput.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py remove inputs $1
fi
