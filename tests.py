import os
import random
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


print(f"Test1: should print the calculator's usage instructions")
print(f'{run_python_file("calculator", "main.py")}')
print(f"\n-----\n")

print(f"Test2: should run the calculator... which gives a kinda nasty rendered result")
print(f'{run_python_file("calculator", "main.py", ["3 + 5"])}')
print(f"\n-----\n")

print(f"Test3: should run the calculator's test script")
print(f'{run_python_file("calculator", "tests.py")}')
print(f"\n-----\n")

print(f"Test4: should return an error")
print(f'{run_python_file("calculator", "../main.py")}')
print(f"\n-----\n")

print(f"Test5: should return an error")
print(f'{run_python_file("calculator", "nonexistent.py")}')
print(f"\n-----\n")

print(f"Test6: should return an error")
print(f'{run_python_file("calculator", "lorem.txt")}')

