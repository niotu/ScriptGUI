import argparse
from os import walk

p = argparse.ArgumentParser(prog="checker.py", description="program check for .error files")

p.add_argument("directory")

directory = p.parse_args().directory

files = list(walk(directory))

for file in files[0][2]:
    if file.split(".")[-1] == "error":
        print(directory, f"ERROR in {file}")
        raise ValueError

print(f'all good in {directory}')
