import os
import shutil

def organize_files(folder_path):
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            extension = file.split(".")[-1]

            folder_name = extension + "_files"
            folder_path_ext = os.path.join(folder_path, folder_name)

            if not os.path.exists(folder_path_ext):
                os.makedirs(folder_path_ext)

            shutil.move(file_path, os.path.join(folder_path_ext, file))

folder = input("Enter the folder path: ").strip('"')
organize_files(folder)

print("Files organized successfully.")