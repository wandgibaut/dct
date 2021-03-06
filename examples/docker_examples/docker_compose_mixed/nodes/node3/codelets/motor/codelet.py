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


class MotorCodelet(dct.PythonCodelet):

    def calculate_activation(self):
        # print("new Activation")
        return 0.0

    def proc(self, activation):
        mem = dct.get_memory_objects(self.root_codelet_dir, 'motor-input-memories/behavioral-memory', 'inputs')
        # dct.set_memory_objects(self.root_codelet_dir, 'final-memory', 'I', mem['I'], 'outputs')
        print(mem['I'])


if __name__ == '__main__':
    codelet = MotorCodelet(name='motorCodelet')
    threading.Thread(target=codelet.run).start()
    # codelet.run()
