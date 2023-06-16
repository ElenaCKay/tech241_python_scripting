# Working with JSON

# High level readable language
#import json

# json = json.loads(open('example.json').read()) # Use the json library open the file and read it.
# value = json['name']  # From the example.json grabbing the value of name
# print(value)
# print(type(json)) # It is no longer JSON it is now dict

# More Advanced

import json, os

# script to make an absolute of the JSON file

script_dir = os.path.dirname(__file__)
print("The script is located at " + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("the script absolute path is: " + script_absolute_path)

# Script to parse JSON

json = json.loads(open(script_absolute_path).read())
value = json["name"]
print(value)

# Loop through the JSON

for key in json:
    value = json[key]

    # .format puts the parameter into the curly brackets.
    print("The key and value are {} = {}".format(key, value))