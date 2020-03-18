import json
import sys


def change_memory(memoryFileName, memoryField, valueToSet):
	with open('../../testMemory/' + memoryFileName +'.json', 'r+') as json_data:
		jsonData = json.load(json_data) 
		jsonData[memoryField] = valueToSet # I or eval
		print(jsonData[memoryField])
		
		json_data.seek(0) #rewind
		json.dump(jsonData, json_data)
		json_data.truncate()

def read_memory(memoryFileName, memoryField):
	with open('../../testMemory/' + memoryFileName +'.json', 'r+') as json_data:
		jsonData = json.load(json_data) 
		print(jsonData[memoryField])


def convert(string): 
    li = list(string.split(";")) 
    return li 


if __name__ == '__main__':
    args = sys.argv[2:]
    readOrMod = sys.argv[1]
    if len(args) >= 2:
        memoryFileName = args[0]
        memoryField = args[1]
        if readOrMod == 'read':
            read_memory(memoryFileName, memoryField)
        elif readOrMod == 'mod':
            valueToSet = args[2]
            change_memory(memoryFileName, memoryField, valueToSet)
        else:
            print("option do not exists!")
    
    else:
        print(len(args))
        print('Error! Wrong number of arguments!')
        sys.exit()

