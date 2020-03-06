#!/bin/bash

# usage: ./setLoop.sh <arg>
# where <arg> is true or false
# example: ./setLoop.sh true

if [ $# -eq 0 ]
    then
        echo "No argument supplied!

usage: ./setLoop.sh <arg>"
    else
        python3 changeField.py loop $1
fi
