#!/bin/bash

# Returns the codelet threshold
# usage: ./getThreshold.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py threshold

# use the following commands to retrieve and store the result: 
# result=$(./getThreshold.sh)
# echo $result
