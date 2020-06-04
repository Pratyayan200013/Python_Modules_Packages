import json
import requests
r = requests.get(
    "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-JSON/states.json")
# print(r.text)
# As it is a JSON response so we will use r.json() instead of r.text
#py_dict = r.json()
# r.json has converted the JSON response into a python dictionary and it is stored in the variable called py_dict and now it can be used as a python dictionary
# print(py_dict)
'''with open("states.json", 'w') as f:
    f.write(r.text)'''
# The write() argument should be a string and not a dictionary and so we used r.text as it gives the JSON response i.e a json string..

# json --> Java Script Object Notation.. It is a part of Python's standard library

'''with open("states.json", 'r') as read_file:
    developers = json.load(read_file)'''
# json.load() --> It loads the json encoded data from a json file and converts it into a python dictionary..
# developers is the variable in which the python dictionary is stored and now we can use it as a python dict..
# print(developers)
# print(developers['states'])
'''for i in developers['states']:
    print(i['name'])'''
'''for i in developers['states']:
    del(i['area_codes'])
    print(i)'''

# r.text gives us a JSON response i.e a json string..
dev = json.loads(r.text)
# json.loads() --> It converts a json string into a python object i.e a python dictionary
# print(dev)
# dev is the variable where the python object or dictionary is stored and we use it just like a Python dictionary
'''for i in dev['states']:
    print(i['abbreviation'])'''
for i in dev['states']:
    del(i['abbreviation'])
    # print(i)
# print(dev)

# dev is a python object or python dictionary
'''with open("new_states.json", 'w') as out_line:
    json.dump(dev, out_line)'''
# json.dump() --> It writes a python object or a python dictionary into a json file..
# Here the python object or the python dictionary dev is getting written on a json file called out_line..

# dev is a python object or a python dictionary..
json_string = json.dumps(dev, indent=2)
# json.dumps() --> It converts a python object or a python dictionary into a json string..
print(json_string)

'''Python    <----------------->     JSON
   True                              true
   False                             false
   None                              null
   array                             list
   int                               number(int)
   float                             number(real)
   str                               string
   dict                              object'''
