# ****************************************************************************#
# Copyright (c) 2020  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the MIT License                       #
# which accompanies this distribution, and is available at                    #
# https://opensource.org/licenses/MIT                                         #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
# ****************************************************************************#
import time
import threading
import os
import dct


class BehavioralCodelet(dct.PythonCodelet):

    def calculate_activation(self):
        # print("new Activation")
        return 0.0

    def proc(self, activation):
        mem = dct.get_memory_objects(self.root_codelet_dir, 'behavioral-input-memories/perceptual-memory', 'inputs')
        dct.set_memory_objects(self.root_codelet_dir, 'motor-behavioral-memory', 'I', mem['I'], 'outputs')


if __name__ == '__main__':
    codelet = BehavioralCodelet(name='behavioralCodelet')
    threading.Thread(target=codelet.run).start()
    # codelet.run()
