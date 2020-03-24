#!/bin/bash

# usage: ./addInput.sh <arg>
# where <arg> is a string with the inputs to set
# example: ./addInput.sh '{"key": "value"}'

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setInputs.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py add inputs "$1"
fi


# must format like this: '{"key": "value"}' when called
