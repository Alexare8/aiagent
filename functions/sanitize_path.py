import os

def sanitize_path(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not (abs_path == abs_working_directory or abs_path.startswith(abs_working_directory + os.sep)):
        raise PermissionError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    return abs_path