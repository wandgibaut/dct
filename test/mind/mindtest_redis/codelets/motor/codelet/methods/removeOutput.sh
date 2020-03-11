#!/bin/bash

# usage: ./removeOutput.sh <field> <value>
# example: ./removeOutput.sh ip/port 127.0.0.1:6000

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./removeOutput.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py remove outputs $1
fi

