#1
import os
def list_directories_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files

#2
def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

#3
def path_details(path):
    exists = os.path.exists(path)
    if exists:
        directory, filename = os.path.split(path)
        return exists, directory, filename
    else:
        return exists, None, None

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

#5
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

#6
def generate_alphabet_files(path):
    for letter in range(65, 91):
        with open(os.path.join(path, f"{chr(letter)}.txt"), 'w') as file:
            pass

#7
import shutil
def copy_file(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    else:
        return False