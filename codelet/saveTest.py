import json


fake_person = {
    'name': 'none',
    'activation': '0.0',
    'threshold': '0.0',
    'timestep': '300',
    'enable': 'true',
    'loop': 'true',
    'lock': 'false',
    'inputs': [
        {'name': 'testInputMemory',
        'isAnObject': 'false',
        'ip/port': '127.0.0.1:3000'}
        ],
    'outputs': [
        {'name': 'testOutputMemory',
        'isAnObject': 'false',
        'ip/port': '127.0.0.1:3000'}
        ],
    'broadcast': [
        {'name': 'testBroadcastMemory',
        'isAnObject': 'false',
        'ip/port': '127.0.0.1:3000'}
        ]
}


with open('fields.json', 'w') as outfile:
    json.dump(fake_person, outfile)


