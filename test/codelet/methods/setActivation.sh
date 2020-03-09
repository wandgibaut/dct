#!/bin/bash

# usage: ./setActivation.sh <arg>
# where <arg> is the activation to set
# example: ./setActivation.sh 0.5

# TODO: check boundaries

root_codelet_dir=/home/codelet

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setActivation.sh <arg>"
    else
        python3 $root_codelet_dir/methods?changeField.py activation $1
fi
