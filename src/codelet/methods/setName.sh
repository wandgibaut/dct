#!/bin/bash

# usage: ./setName.sh <arg>
# where <arg> is the name to set
# example: ./setName.sh codeletName

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setName.sh <arg>"
    else
        python3 changeField.py name $1
fi

