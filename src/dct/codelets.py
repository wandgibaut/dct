# ****************************************************************************#
# Copyright (c) 2022  Wandemberg Gibaut                                       #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the MIT License                       #
# which accompanies this distribution, and is available at                    #
# https://opensource.org/licenses/MIT                                         #
#                                                                             #
# Contributors:                                                               #
#      W. Gibaut                                                              #
#                                                                             #
# ****************************************************************************#

import ujson as json
import sys
import os
import time

class PythonCodelet:
    def __init__(self, name=None, root_codelet_dir=None):
        if root_codelet_dir is None:
            os.chdir(os.path.dirname(__file__))
            root_codelet_dir = os.getcwd()
        self.root_codelet_dir = root_codelet_dir
        self.name = name

    def read_field(self, field):
        with open(self.root_codelet_dir + '/fields.json', 'r') as json_data:
            jsonData = json.load(json_data)
            value = jsonData[field]
        return value

    def change_field(self, field, value):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = value
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def add_entry(self, field, data):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            vector = jsonData[field]
            vector.append(json.loads(data))
            jsonData[field] = vector

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def remove_entry(self, field, name):
        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            vector = jsonData[field]

            for i in vector:
                for k, v in i.items():
                    if v == name:
                        vector.remove(i)
                        return i

            jsonData[field] = vector
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    def set_field_list(self, field, dataList):
        jsonList = []
        for dataString in dataList:
            jsonList.append(json.loads(dataString))

        with open(self.root_codelet_dir + '/fields.json', 'r+') as json_data:
            jsonData = json.load(json_data)
            jsonData[field] = jsonList
            # print(jsonData[field])

            json_data.seek(0)  # rewind
            json.dump(jsonData, json_data)
            json_data.truncate()

    @staticmethod
    def convert(self, string):
        li = list(string.split(";"))
        return li

    def run(self):
        while self.read_field('enable') == 'true':
            while self.read_field('lock') == 'false':
                activation = self.calculate_activation()
                self.proc(activation)
                time.sleep(float(self.read_field('timestep')))

        sys.exit()

    def calculate_activation(self):
        ########################################
        # Default Activation ##
        print("default activation")
        return 0

    def proc(self, activation):
        ########################################
        # Default proc ##
        print("default proc")