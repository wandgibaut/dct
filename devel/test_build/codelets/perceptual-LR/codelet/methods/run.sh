#!/bin/bash

#*****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the GNU Lesser Public License v3      #
# which accompanies this distribution, and is available at                    #
# http://www.gnu.org/licenses/lgpl.html                                       #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
#*****************************************************************************#

root_codelet_dir=/home/codelet

run=$($root_codelet_dir/methods/getLoop.sh)

#echo $n
#echo $#
if [ $# -ne 0 ] 
    then
        echo "initiating servers!"
        for var in "$@"
        do
            python3 $root_codelet_dir/server.py "$var"  &
        done
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