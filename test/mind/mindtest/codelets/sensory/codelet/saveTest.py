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
        {'name': 'test-input/memories/testInputMemory',
        'type': 'mongo',
        'ip/port': 'mongodb://mongodb:27017/'}
        ],
    'outputs': [
        {'name': 'testOutputMemory',
        'type': 'mongo',
        'ip/port': 'mongodb://mongodb:27017/'}
        ],
    'broadcast': [
        {'name': 'testBroadcastMemory',
        'type': 'mongo',
        'ip/port': 'mongodb://mongodb:27017/'}
        ]
}


with open('fields.json', 'w') as outfile:
    json.dump(fake_person, outfile)


