import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, directory))
    if not (abs_path == abs_working_directory or abs_path.startswith(abs_working_directory + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    file_descriptions = []
    for file in os.listdir(abs_path):
        file_path = os.path.join(abs_path, file)
        file_descriptions.append(f" - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

    return "\n".join(file_descriptions)