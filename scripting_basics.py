# Basics of scripting in Python

# Libraries and Modules
# Module is a collection of functions
# Library is a collection of modules

# Seven core modules in Python

# import sys # System
#
# print(sys.version) # Gives the python version
#
# import os # Operating system for files and folders
#
# print(os.getcwd()) # Current working directory

# import subprocess # Lets this file work with other files
#
# # Can create infinite loops
# subprocess.run(["python", "hello_world.py"]) # Runs another file

# import math # For maths things
#
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is " + pi_string)
#
# import random # For random things
#
# randnum = random.randrange(1, 10)
# print(randnum)

# import datetime
#
# what_is_the_date = datetime.datetime.now() # what is the date now
# print(what_is_the_date)

import json # Used with APIs

x = {
    "name": "John",
    "age": 30,
    "city": "Liverpool"
}

y = json.dumps(x) # Turns dictionary into valid JSON string

print(y)

