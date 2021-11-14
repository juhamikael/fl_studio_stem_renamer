import os
from subprocess import run
from functions import rename_remove_date, move_files
import configparser

# Configuration
read_config = configparser.ConfigParser()
read_config.read("./config.ini")
defaulPath = read_config.get("Path", "default_path")
customPath = read_config.get("Path", "custom_path")
path = f"{customPath}{defaulPath}"
print("Current path =", path)

# Variables
project_name = input(f"Type your project name: ")
search_string = project_name.replace(" ", "_")
search_string_to_lower = search_string.lower()
new_folder = f"cd {path} &&" \
             f"mkdir {search_string_to_lower}"
new_path = f"{path}/{search_string_to_lower}"
# Ignore lowercase

# Changing working path so new folder can be made
os.chdir(path)
run(new_folder, shell=True)

first_ls = os.listdir(path)

# Move files
move_files(first_ls, project_name, new_path)

# Rename files (remove date from the name)
os.chdir(new_path)
second_ls = os.listdir(new_path)
rename_remove_date(second_ls, search_string_to_lower, project_name)
