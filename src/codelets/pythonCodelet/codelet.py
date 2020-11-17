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
import os
import dct
import threading

class TestCodelet(dct.PythonCodelet):

    def calculate_activation(self):
        print("new Activation")
        return 0.0

    def proc(self, activation):
        print("new Proc")


if __name__ == '__main__':
    codelet = TestCodelet(name='defaultCodelet')
    threading.Thread(target=codelet.run).start()
