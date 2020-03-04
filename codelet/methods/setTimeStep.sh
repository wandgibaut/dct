#!/bin/bash

# usage: ./setTimeStep.sh <arg>
# where <arg> is the timestep to set
# example: ./setTimeStep.sh timestep

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setTimeStep.sh <arg>"
    else
        python3 changeField.py timestep $1
fi

