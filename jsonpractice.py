#import of json class library
import json

#create data dictionary
data = {
    'name': 'Theo Molin',
    'age' : 28,
    'city': 'Revere,MA',
    'interests': ['Zouking', 'Bachata', 'Argentine Tango', 'BBoying', 'Choreo'],
    'is_student' : False
}
#objective is to convert py to json
#open file to be written
with open('data.json', 'w') as json_file:# create json file named data.json
#convert to json using dump
    json.dump(data,json_file, indent = 4)
#print confirmation
print("Data has been written to data.json")

#open file to be read
with open('data.json','r') as json_file:
#create object: loaded_data, data will come from json file
    loaded_data = json.load(json_file)
#print confirmation
print("Successfully able to read data.json")
#print object since object will be read
print(loaded_data)

#alter key values in data
loaded_data['age'] = 30
loaded_data['interests'].append('Plushies')

#Rewrite json file to implement changes
with open('data.json','w') as json_file:
    json.dump(data,json_file, indent = 4)

#print confirmation of changes
print(loaded_data)
print("json file has been rewritten")