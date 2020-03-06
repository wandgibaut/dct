#!/bin/bash

# usage: ./removeOutput.sh <field> <value>
# example: ./removeOutput.sh ip/port 127.0.0.1:6000


if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./removeOutput.sh <arg>"
    else
        python3 changeField.py remove outputs $1
fi

