import os, subprocess
from functions.sanitize_path import sanitize_path

def run_python_file(working_directory, file_path, args=[]):
    try:
        path_name = sanitize_path(working_directory, file_path)
    except PermissionError as e:
        return e.args[0]

    if not os.path.exists(path_name):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.splitext(path_name)[1] == ".py":
        return f'Error: "{file_path}" is not a Python file.'

    command = ["uv", "run", path_name] + args

    try:
        completed_process = subprocess.run(command, capture_output=True, cwd=os.path.abspath(working_directory), timeout=30, text=True)

        report = []
        if completed_process.stdout != "" or completed_process.stderr != "":
            report.append(f'STDOUT:{completed_process.stdout}')
            report.append(f'STDERR:{completed_process.stderr}')
        else:
            report.append(f'No output produced.')
        report.append(f'Process exited with code {completed_process.returncode}')
        return "\n".join(report)

    except Exception as e:
        return f"Error: executing Python file: {e}"