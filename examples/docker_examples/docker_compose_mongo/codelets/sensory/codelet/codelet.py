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
import os
import threading
import dct


class SensoryCodelet(dct.PythonCodelet):

    def calculate_activation(self):
        # print("new Activation")
        return 0.0

    def proc(self, activation):
        mem = dct.get_memory_objects(self.root_codelet_dir, 'perceptual-input-memories/sensory-memory', 'outputs')
        if mem['I'] is None:
            mem['I'] = -1
        I = int(mem['I']) + 1
        dct.set_memory_objects(self.root_codelet_dir, 'perceptual-input-memories/sensory-memory', 'I', str(I), 'outputs')


if __name__ == '__main__':
    print(os.getenv('ROOT_CODELET_DIR'))
    codelet = SensoryCodelet(name='sensoryCodelet')
    threading.Thread(target=codelet.run).start()
    #codelet.run()

