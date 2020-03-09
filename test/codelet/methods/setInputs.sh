#!/bin/bash

# usage: ./setInputs.sh <arg>
# where <arg> is a string with the inputs to set
# example: ./setInputs.sh [{"name":....}, {"name":....}]

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setInputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list inputs "$1"
fi
