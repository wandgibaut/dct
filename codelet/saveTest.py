import json


fake_person = {
    'name': 'none',
    'activation': '0.0',
    'threshold': '0.0',
    'timestep': '300',
    'enable': 'true',
    'loop': 'true',
    'lock': 'false',
    'inputs': [],
    'outputs': [],
    'broadcast': []
}


with open('fields.json', 'w') as outfile:
    json.dump(fake_person, outfile)


