#!/bin/bash

# Returns the codelet name
# usage: ./getName.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py name

# use the following commands to retrieve and store the result: 
# result=$(./getName.sh)
# echo $result
