#!/bin/bash

# usage: ./setLock.sh <arg>
# where <arg> is true or false
# example: ./setLock.sh true

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setLock.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py lock $1
fi
