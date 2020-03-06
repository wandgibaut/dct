#!/bin/bash

# Returns if the codelet is locked
# usage: ./getLock.sh

result= python3 readField.py lock
# use the following commands to retrieve and store the result: 
# result=$(./getLock.sh)
# echo $result
