#!/bin/bash

# usage: ./setOutputs.sh <arg>
# where <arg> is a string with the outputs to set
# example: ./setOutputs.sh [{"name":....}, {"name":....}]


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setOutputs.sh <arg>"
    else
        python3 changeField.py outputs $1
fi
