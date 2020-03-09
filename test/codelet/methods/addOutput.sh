#!/bin/bash

# usage: ./addOutput.sh <arg>
# where <arg> is a string with the outputs to set
# example: ./addOutput.sh '{"key": "value"}'

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setOutputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py add outputs "$1"
fi


# must format like this: '{"key": "value"}' when called
