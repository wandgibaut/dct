#!/bin/bash

# usage: ./setName.sh <arg>
# where <arg> is the name to set
# example: ./setName.sh codeletName

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setName.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py name $1
fi

