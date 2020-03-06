import json


memory_struct = {
    'name': 'none',
    'ip/port': '127.0.0.1:8080',
    'isAnObject': 'false',
    'I': {},
    'eval': '0.0'
}


with open('simpleMemory.json', 'w') as outfile:
    json.dump(memory_struct, outfile)

