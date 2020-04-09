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

for i in addInput.sh addOutput.sh removeInput.sh removeOutput.sh stop.sh start.sh run.sh proc.sh calculateActivation.sh accessMemoryObjects.sh enable.sh disable.sh; do
	touch $i

done

for i in Activation.sh Threshold.sh Inputs.sh Outputs.sh Broadcast.sh Loop.sh TimeStep.sh Name.sh Lock.sh; do
	touch set$i
	touch get$i

done



