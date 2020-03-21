#!/bin/bash

# Returns the codelet inputs
# usage: ./getInput.sh (optional) <arg1> <arg2>

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
then
    result= python3 $root_codelet_dir/methods/readField.py inputs

elif [ $# -eq 1 ]
then
    result= python3 $root_codelet_dir/methods/readField.py inputs $1

elif [ $# -eq 2 ]
then
    result= python3 $root_codelet_dir/methods/readField.py inputs $1 $2

else
    echo "Wrong number of arguments!

usage: ./getInput.sh (optional) <arg1> <arg2>"

fi


# use the following commands to retrieve and store the result: 
# result=$(./getInputs.sh)
# echo $result

#list of all
# name
# name index
