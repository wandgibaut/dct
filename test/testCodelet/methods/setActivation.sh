#!/bin/bash

# usage: ./setActivation.sh <arg>
# where <arg> is the activation to set
# example: ./setActivation.sh 0.5

# TODO: check boundaries

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setActivation.sh <arg>"
    else
        python3 changeField.py activation $1
fi
