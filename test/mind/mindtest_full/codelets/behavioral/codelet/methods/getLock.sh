#!/bin/bash

# Returns if the codelet is locked
# usage: ./getLock.sh

root_codelet_dir=/home/codelet

result= python3 $root_codelet_dir/methods/readField.py lock
# use the following commands to retrieve and store the result: 
# result=$(./getLock.sh)
# echo $result
