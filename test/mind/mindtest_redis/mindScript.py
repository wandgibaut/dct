import json
from pymongo import MongoClient

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


# mount : receber lista de codelets
# verificar inputs, outputs e tipo de codelet
# montar metodos de acesso e ligar tudo 

#padrão pra nome da base e da collection
# base: 'database-raw-memory'
# collection: '<tipo: sensory, perceptual...>-<anotação: nome do codelet, grupo de codelets...>-input-memories'

# TODO: consider redis and tcp/ip types

def mount(list_of_codelets):
    for codelet in list_of_codelets:
        with open('codelets/'+ codelet + '/codelet/fields.json', 'r+') as json_data:  # abrir o fields
		    jsonData = json.load(json_data)
		    inputs = jsonData['inputs']
            outputs = jsonData['outputs']
            codelet_name = jsonData['name']

            for inputMemory in inputs:
                if inputMemory['type'] == 'mongo' 
                    client = MongoClient(inputMemory['ip/port']) # METODO: vai no ip
                    base = client['database-raw-memory']
                    inMem = base[convert(inputMemory[name])[0]] # define base, collection (input name)
                    mem = inMem.find_one({'name': inputMemory['name']}) # e checa se existe uma memoria com esse name

                    if(mem == None):  # se sim, deixa quieto, se não, cria
                        memory = {'name': convert(inputMemory[name])[1],'ip/port': inputMemory['ip/port'],'type': 'mongo','I': None,'eval': 0.0}
                        outMem.insert_one(memory)
       
        # pegar os inputs e gerar uma memoria de name: name
            # METODO: vai no ip
            # define base, collection (input name)
            # e checa se existe uma memoria com esse _id
            # se sim, deixa quieto, se não, cria
        #


def convert(string): 
    li = list(string.split("/")) 
    return li 

if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) == 1:
		activation = args[0]
		main(activation)
	
	else:
		print(len(args))
		print('Error! Wrong number of arguments!')
		sys.exit()

