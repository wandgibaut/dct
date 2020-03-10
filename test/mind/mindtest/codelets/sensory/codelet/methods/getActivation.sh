#!/bin/bash

# Returns the codelet activation
# usage: ./getActivation.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py activation

# use the following commands to retrieve and store the result: 
# result=$(./getActivation.sh)
# echo $result
