import os
import subprocess

# Stores file path to the current file
script_dir = os.path.dirname(__file__)
print(script_dir)
# Stores the filepath to the script you want to run
script_absolute_path = os.path.join(script_dir + "\shell_script.sh")
print(script_absolute_path)
# Calls the shell file and runs it
subprocess.call(["sh", script_absolute_path]) # sh is the language (shell)