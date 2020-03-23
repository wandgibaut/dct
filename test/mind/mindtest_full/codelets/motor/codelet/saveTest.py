import json


memory = {
    "name": "motor-memory",
    "ip/port": "172.28.1.1:9999",
    "type": "tcp",
    "I": None,
    "eval": 0.0
}


with open('motor-memory.json', 'w') as outfile:
    json.dump(memory, outfile)


