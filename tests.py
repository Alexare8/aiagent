import os
import random
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

if os.path.exists(os.path.abspath("calculator/pkg/morelorem.txt")):
    print(f"Deleting morelorem.txt before testing")
    os.remove("./calculator/pkg/morelorem.txt")

print(f'test1: write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("\n-----\n")

print(f'test2: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("\n-----\n")

print(f'test3: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("\n-----\n")

print(f'test4: write_file("calculator", "pkg/morelorem.txt", "Something else entirely") when file already exists')
print(write_file("calculator", "pkg/morelorem.txt", "Something else entirely"))
print("\n-----\n")