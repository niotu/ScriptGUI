from os import walk
import sys
from argparse import ArgumentParser
from shutil import copy
from PyQt5.QtWidgets import QFileDialog, QApplication

p = ArgumentParser(prog="checker.py", description="program check for .error files")
p.add_argument("directory")
p.add_argument("curr")
directory = p.parse_args().directory
curr = p.parse_args().curr

dailApp = QApplication(sys.argv)

dial = QFileDialog.getExistingDirectory(None, "Choose dir", directory + curr)
print(dial)
dir = dial

files = list(walk(dir))[0][2]
print(files)

for file in files:
    print(dir + '/' + file, directory[:-1])
    copy(dir + '/' + file, directory[:-1])
