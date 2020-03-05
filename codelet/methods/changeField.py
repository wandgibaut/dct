import json
import sys

def change_field(field, value):
	with open('../fields.json', 'r+') as json_data:
		jsonData = json.load(json_data)
		jsonData[field] = value
		print(jsonData[field])
		
		json_data.seek(0) #rewind
		json.dump(jsonData, json_data)
		json_data.truncate()
	
def add_entry(field, data):
	with open('../fields.json', 'r+') as json_data:
		jsonData = json.load(json_data)
		vector = jsonData[field]
		vector.append(json.dumps(data))
		jsonData[field] = vector
		
		print(jsonData[field])
		
		json_data.seek(0) #rewind
		json.dump(jsonData, json_data)
		json_data.truncate()
		



if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 2:
		field = args[0]
		value = args[1]
		change_field(field, value)
	
	elif len(args) == 3:
		if args[0] == 'add':
			field = args[1]
			data = args[2]
			print(data)
			add_entry(field, data)

		elif args[0] == 'remove':
			field = args[1]
			data = args[2]
			#remove_entry(field, data)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

