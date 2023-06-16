import os
import sys
import json

# How to check JSON is valid

#If there is more then one file in the terminal
if len(sys.argv) > 1:
    # Check if the second file exists
    if os.path.exists(sys.argv[1]):
        # Read the contents
        file = open(sys.argv[1], "r")
        #See if you can load it which means it will be valid
        json.load(file)
        #Close it now you have checked it
        file.close()
        print("JSON is VALID!")
    else:
        print(sys.arg[1] + "not found")
else:
    print("Usage: check_json.py <file>")

#If invalid the terminal will give you an error for the specified JSON file and where the error is