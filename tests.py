from functions.get_files_info import get_files_info

print(f'test1: get_files_info("calculator", ".")')
print(get_files_info("calculator", "."))
print("\n-----\n")

print(f'test2: get_files_info("calculator", "pkg")')
print(get_files_info("calculator", "pkg"))
print("\n-----\n")

print(f'test3: get_files_info("calculator", "/bin")')
print(get_files_info("calculator", "/bin"))
print("\n-----\n")

print(f'test4: get_files_info("calculator", "../")')
print(get_files_info("calculator", "../"))