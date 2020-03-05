#!/bin/bash

# usage: ./setInputs.sh <arg>
# where <arg> is a string with the inputs to set
# example: ./setInputs.sh [{"name":....}, {"name":....}]


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setInputs.sh <arg>"
    else
        python3 changeField.py inputs $1
fi
