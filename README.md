# Python Scripting

## What is scripting?

It is the process of writing and executing scripts using python. A script is a sequence of instructions written in a scripting language that can be executed with the need for compilation. 

Do do this write a series of commands or instructions in a plan text file with a .py extension. They can be executed by the Python interpreter.
Scripts are always one file. 

### Why is scripting important for DevOps engineers?

Scripts are used for automating tasks, performing repetitive actions and manipulating data.
Different to programming which has a wide scope and is used for a lot of things. Scripts are easy to read and less technical. Scripts are specific and not flexable. High level languages.
Python is easy, has lots of languages, large community (open source) and language interoperability. Automation and configuration.

### Example 
- Python script to query a database
- Python script to execute a shell command or script
- Query logs for alerts
- Python script to take a backup
- Python script for K8 containers
- Python script to fetch I.P's of an autoscaling group
- Lambda function to stop instances on a weekend
- Python script for ETL jobs
- Find the expiry date of an SSL certificate
- Develop CLI applications using Python
- Automating CRUD
- Custom scripts for config management

### Important Python Modules for DevOps
- os (Interacting with the operating system)
- platform (Access to underlying platform data)
- subprocess (Subprocess management)
- sys (System specific parameters and functions)
- psutil (Process and system utilities)
- re (Regular Expression Operations)
- scapy (Packet manipulation)
- Requests (HTTP library)
- urllib3 (HTTP client)
- logging (Error logging)
- getpass (Portable password input)
- boto3 (AWK Software development kit, SDK. Allows interaction with AWS from Python)
- paramiko (SSH)
- JSON (JSON encoder and decoder
- PyYAML (YAML parser & emitter for Python)
- pandas (Data science, but useful for automating CSV's)
- smtplib (STMP)

### Scripting basics

A module is a collection of functions and a library is a collection of modules.

There are 7 core modules / libraries in python:

1. sys - Stands for system and it is for anything to do with the system
2. os - Operating system -> all to do with files and folders
3. subprocess -> Lets the current file work with other files
4. math -> all maths related things
5. random -> all random related things
6. datetime -> all to do with dates and times 
7. json -> used as a translator for APIs

## JSON

JavaScript Object Notation. It is a high level, human-readable language. It is used to transport data such as from a repo to an API. It can transport data to different languages and acts as a translater. 

JSON works with key value pairs like dictionaries / objects but it doesnt need a variable name. The extension on json files is .json

Parsing -> turning a string into a data structure and vice versa. Read a JSON file, parse it and send it to python or the other way round.

To remove human error you need to make a script to parse files. The json. load() is used to read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary.


It will only work if the JSON file is valid. So you need to make a script to check if the JSON is valid before you send it. An example of this is in check_json.py, it needs to be run in the terminal with the first arg as check_json.py and then the file you want to check.