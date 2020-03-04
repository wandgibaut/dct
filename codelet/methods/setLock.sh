#!/bin/bash

# usage: ./setLock.sh <arg>
# where <arg> is true or false
# example: ./setLock.sh true

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setLock.sh <arg>"
    else
        python3 changeField.py lock $1
fi
