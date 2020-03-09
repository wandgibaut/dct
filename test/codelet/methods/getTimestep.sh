#!/bin/bash

# Returns the codelet timestep
# usage: ./getTimestep.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py timestep

# use the following commands to retrieve and store the result: 
# result=$(./getTimestep.sh)
# echo $result
