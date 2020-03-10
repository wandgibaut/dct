#!/bin/bash

# usage: ./disable.sh

root_codelet_dir=/home/codelet

python3 $root_codelet_dir/methods/changeField.py enable false
