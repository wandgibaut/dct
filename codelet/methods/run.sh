#!/bin/bash

run=$(./getLoop.sh)

while $run
do
    activation=$(../calculateActivation.sh)
    memories=$(../accessMemoryObjects.sh)
    
    ../proc.sh $activation $memories

    run=$(./getLoop.sh)
    timestep=$(./getTimestep.sh)
    sleep($timestep)
   
done