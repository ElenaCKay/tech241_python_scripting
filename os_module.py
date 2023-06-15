# Using os to do things

import os

#os.system('echo "Hello world"')

# make and change directories

directory = "test_dir" # Directory name

parent_dir = "C:/Users/elena/PycharmProjects" # Parent name

path = os.path.join(parent_dir, directory) # Joining them together to make a path
#
# os.mkdir(path)

# Putting a file in the new dir

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1: # w stands for write
    to_file = "Contents of file is written here"
    file1.write(to_file)

print(f"File {filename} created in {directory} folder")