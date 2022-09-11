import os
from subprocess import run
import configparser
import shutil


class StemRenamer:
    def __init__(self):
        self.path = self.read_config_()
        self.project_name = input(f"Type your project name: ")
        self.search_string = self.project_name.replace(" ", "_")
        self.search_string_to_lower = self.search_string.lower()
        self.new_folder = f"cd {self.read_config_()} && " \
                          f"mkdir {self.search_string_to_lower}"
        self.new_path = fr"{self.path}\{self.search_string_to_lower}"

    @staticmethod
    def read_config_():
        read_config = configparser.ConfigParser()
        read_config.read("./config.ini")
        defaulPath = read_config.get("Path", "default_path")
        customPath = read_config.get("Path", "custom_path")
        path = f"{customPath}{defaulPath}"
        return path

    def rename_files(self, file_list: list, inp):
        os.chdir(self.new_path)
        files_to_rename = []
        for file in file_list:
            # if file string contains search string
            if file.startswith(self.project_name):
                files_to_rename.append(file)

        for file in files_to_rename:
            date_name_len = 21
            total_worthless_len = len(inp) + date_name_len
            os.rename(file, file[total_worthless_len:])

    def run_create_folder(self):
        print(self.new_folder)
        os.chdir(self.path)
        run(self.new_folder, shell=True)

    def run_move_files(self):
        project_stems_to_move = []
        file_list = os.listdir(self.path)
        for file in file_list:
            if file.startswith(self.project_name):
                project_stems_to_move.append(file)
        for file in project_stems_to_move:
            shutil.move(file, self.new_path)

    def run_rename_files(self):
        file_list = os.listdir(self.new_path)
        self.rename_files(file_list, self.search_string_to_lower)

    def run(self):
        self.run_create_folder()
        self.run_move_files()
        self.run_rename_files()


sr = StemRenamer()
sr.run()
