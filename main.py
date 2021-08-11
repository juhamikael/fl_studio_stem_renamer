import os
import shutil
from subprocess import run
from functions import rename_remove_date, move_files

import configparser

# Configuration
config = configparser.ConfigParser()
read_config = configparser.ConfigParser()
read_config.read("./application/config.ini")
path = read_config.get("Path", "FL_Studio_data_path")

# Variables
project_name = input(f"Type your project name: ")
search_string = project_name.replace(" ", "_")
search_string_to_lower = search_string.lower()
new_folder = f"cd {path} &&" \
             f"mkdir {search_string_to_lower}"
new_path = f"{path}/{search_string_to_lower}"

# Changing working path so new folder can be made
os.chdir(path)
run(new_folder, shell=True)

# Move file
first_ls = os.listdir(path)
move_files(first_ls, project_name, new_path)

# Rename files (remove date from the name)
os.chdir(new_path)
second_ls = os.listdir(new_path)
rename_remove_date(second_ls, search_string_to_lower, project_name)
