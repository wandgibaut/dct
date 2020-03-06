#!/bin/bash

# usage: ./removeInput.sh <field> <value>
# example: ./removeInput.sh ip/port 127.0.0.1:6000


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./removeInput.sh <arg>"
    else
        python3 changeField.py remove inputs $1
fi
