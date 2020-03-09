#!/bin/bash

# usage: ./setThreshold.sh <arg>
# where <arg> is the threshold to set
# example: ./setThreshold.sh 0.5

# TODO: check boundaries

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setThreshold.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py threshold $1
fi

