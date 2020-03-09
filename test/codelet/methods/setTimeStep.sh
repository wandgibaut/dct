#!/bin/bash

# usage: ./setTimeStep.sh <arg>
# where <arg> is the timestep to set
# example: ./setTimeStep.sh timestep

root_codelet_dir=/home/codelet


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setTimeStep.sh <arg>"
    else
        python3 $root_codelet_dir/methods/changeField.py timestep $1
fi

