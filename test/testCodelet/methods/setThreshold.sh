#!/bin/bash

# usage: ./setThreshold.sh <arg>
# where <arg> is the threshold to set
# example: ./setThreshold.sh 0.5

# TODO: check boundaries

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setThreshold.sh <arg>"
    else
        python3 changeField.py threshold $1
fi

