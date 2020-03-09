#!/bin/bash

# Returns if he codelet is looping
# usage: ./getLoop.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py loop

# use the following commands to retrieve and store the result: 
# result=$(./getLoop.sh)
# echo $result
