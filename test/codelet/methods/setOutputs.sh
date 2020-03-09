#!/bin/bash

# usage: ./setOutputs.sh <arg>
# where <arg> is a string with the outputs to set
# example: ./setOutputs.sh [{"name":....}, {"name":....}]

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setOutputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py list outputs "$1"
fi
