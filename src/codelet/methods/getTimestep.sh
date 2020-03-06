#!/bin/bash

# Returns the codelet timestep
# usage: ./getTimestep.sh

result= python3 readField.py timestep

# use the following commands to retrieve and store the result: 
# result=$(./getTimestep.sh)
# echo $result
