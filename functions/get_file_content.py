import os
from functions.sanitize_path import sanitize_path

def get_file_content(working_directory, file_path):
    try:
        file_path = sanitize_path(working_directory, file_path)
    except PermissionError as e:
        return e.args[0]

    if not os.path.is_file(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'