import os
from functions.sanitize_path import sanitize_path

def write_file(working_directory, file_path, content):
    try:
        path_name = sanitize_path(working_directory, file_path)
    except PermissionError as e:
        return e.args[0]
    
    if not os.path.exists(os.path.dirname(path_name)):
        os.makedirs(os.path.dirname(path_name))

    with open(path_name, "w") as f:
        num_chars_written = f.write(content)
        if len(content) != num_chars_written:
            return f"Error: Something went wrong. {num_chars_written} characters written of {len(content)} characters."
        return f'Successfully wrote to "{file_path}" {num_chars_written} characters written)'
