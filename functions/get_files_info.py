import os
from google.genai import types
from functions.sanitize_path import sanitize_path

def get_files_info(working_directory, directory="."):
    try:
        path_name = sanitize_path(working_directory, directory)
    except PermissionError as e:
        return e.args[0]

    if not os.path.isdir(path_name):
        return f'Error: "{directory}" is not a directory'
    
    file_descriptions = []
    for file in os.listdir(path_name):
        file_path = os.path.join(path_name, file)
        file_descriptions.append(f" - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

    return "\n".join(file_descriptions)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)