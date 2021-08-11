import os
import shutil
from subprocess import run
import configparser

#####
config = configparser.ConfigParser()

read_config = configparser.ConfigParser()
read_config.read("./config.ini")
path = read_config.get("Path", "flstudio_data_path")
fl_date_name_len = 21
#####


project_name = input(f"Type your project name: ")
search_string = project_name.replace(" ", "_")
search_string_to_lower = search_string.lower()

# project_name = "pythontest"

listdir = os.listdir(path)
stems_renamed = [];
for rename_files in listdir:
    rename_files.lower()
    rename_files.replace(" ", "_")

project_stems = []
for file in listdir:
    if file.startswith(project_name):
        project_stems.append(file)

#######################
#Make new folder with project name
new_folder = f"cd {path} &&" \
             f"mkdir {search_string_to_lower}"
os.chdir(path)
run(new_folder, shell=True)

new_path = f"{path}/{search_string_to_lower}"
# cd_new_path = f"cd {path}/{project_name}"

#######################
#Move files to new path
for files in project_stems:
    shutil.move(files, new_path)

os.chdir(new_path)

new_listdir = os.listdir(new_path)
project_stems = []
for file in new_listdir:
    if file.startswith(project_name):
        project_stems.append(file)

for files in project_stems:
    project_name_len = len(search_string_to_lower)
    date_name_len = 21
    total_worthless_len = project_name_len + date_name_len
    os.rename(files, files[total_worthless_len:])

