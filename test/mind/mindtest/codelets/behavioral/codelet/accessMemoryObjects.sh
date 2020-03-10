#!/bin/bash

# he coet outs
# usage: call your program or write directly here
# remember $1 is the activation and $2 is a json object with memories 

############# write your program bellow ##############


if [ $# -eq 4 ]
then
    result= python ../changeMemory.py $1 $2 $3 $4

elif [ $# -eq 3 ]
then
    result= python ../changeMemory.py $1 $2 $3
else
    echo $#
    echo "Wrong number of arguments!

usage: ./accessMemoryObjects.sh <arg1> <arg2> <arg3> (optional) <arg4>"
    
fi


# use the following commands to retrieve and store the result: 
# result=$(./getInputs.sh)
# echo $result

#list of all
# name
# name index

# read or modify
# memory file name
# field to set
# value to set


