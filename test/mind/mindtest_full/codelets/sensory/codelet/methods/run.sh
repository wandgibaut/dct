#!/bin/bash

root_codelet_dir=/home/codelet

run=$($root_codelet_dir/methods/getLoop.sh)

if [ $# -eq 2 ]
    then
        python3 $root_codelet_dir/server.py "$1" "$2"
fi


while $run
do
    activation=$($root_codelet_dir/calculateActivation.sh)
    #memories=$(../accessMemoryObjects.sh)
    
    $root_codelet_dir/proc.sh $activation #$memories

    run=$($root_codelet_dir/methods/getLoop.sh)
    timestep=$($root_codelet_dir/methods/getTimestep.sh)
    sleep $timestep
   
done