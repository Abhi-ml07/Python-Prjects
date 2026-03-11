import os
import shutil

def deorganize_files(folder_path):
    folders = os.listdir(folder_path)

    for folder in folders:
        folder_full_path = os.path.join(folder_path, folder)

        if os.path.isdir(folder_full_path) and folder.endswith("_files"):
            files = os.listdir(folder_full_path)

            for file in files:
                source = os.path.join(folder_full_path, file)
                destination = os.path.join(folder_path, file)

                shutil.move(source, destination)

            os.rmdir(folder_full_path)

folder = input("Enter the folder path: ").strip('"')
deorganize_files(folder)

print("Files restored to the main folder.")