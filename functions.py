# import os
# import shutil
#
#
# def rename_remove_date(file_list: list, inp, project_name):
#     files_to_rename = []
#     for files in file_list:
#         if files.startswith(project_name):
#             files_to_rename.append(files)
#     for files in files_to_rename:
#         date_name_len = 21
#         total_worthless_len = len(inp) + date_name_len
#         os.rename(files, files[total_worthless_len:])
#
#
# def move_files(file_list: list, project_name, new_path):
#     project_stems_to_move = []
#     for file in file_list:
#         if file.startswith(project_name):
#             project_stems_to_move.append(file)
#     for file in project_stems_to_move:
#         shutil.move(file, new_path)
