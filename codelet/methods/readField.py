import json
import sys

def read_field(field):
	with open('../fields.json', 'r') as json_data:
		jsonData = json.load(json_data)
		value = jsonData[field]
	return value


if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		field = args[0]
		print(read_field(field))
	else:
		print('Error! Wrong number of arguments!')

	sys.exit()

