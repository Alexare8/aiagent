import os
from functions.sanitize_path import sanitize_path
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        path_name = sanitize_path(working_directory, file_path)
    except PermissionError as e:
        return e.args[0]

    if not os.path.isfile(path_name):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(path_name, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(1) != "":
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return file_content_string