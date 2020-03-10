import json


fake_person = {
    'name': 'none',
    'rawMemory': '127.0.0.1:27027',
    'coderack': ['codelet1', 'codelet2'],
    'sensoryCodelets': ['codelet1', 'codelet2'],
    'perceptualCodelets': ['codelet1', 'codelet2'],
    'behavioralCodelets': ['codelet1', 'codelet2'],
    'motorCodelets': ['codelet1', 'codelet2'],
    'motivationalCodelets': ['codelet1', 'codelet2'],
    'emotionalCodelets': ['codelet1', 'codelet2'],
    'adaptationCodelets': ['codelet1', 'codelet2'],
    'system1AttentionCodelets': ['codelet1', 'codelet2'],
}

# this covers the system 1 for now

with open('fields.json', 'w') as outfile:
    json.dump(fake_person, outfile)


