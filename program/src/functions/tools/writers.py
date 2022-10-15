import os
import sys
from unittest.util import three_way_cmp
sys.path.append("..")
from functions.tools.checkers import *
from functions.tools.utils import *

def append_line_to_file(write_file, line):
  with open(write_file, 'a') as file:
    file.write(line)
    return 0

def write_line_to_file(write_file, line):
  os.makedirs(os.path.dirname(write_file), exist_ok=True)
  if os.path.exists(write_file):
    append_line_to_file(write_file, line)
    return 0
  else:
    with open(write_file, 'w') as file:
      file.write(line)
      return 0

def copy_files(read_file, write_file):
  while True:
    with open(read_file, 'r') as file:
      for line in file:
        bedue = file.readline()
        write_line_to_file(write_file, line)
        write_line_to_file(write_file, bedue)
        if not bedue:
          return 0
      return 1

def insert_lines_in_file_by_index(read_file, lines_two, index):
  with open(read_file, "r") as file:
    lines = file.readlines()
    lines_one = lines[0:index]
    lines_one.append(lines_two)
    lines_three = lines[index:len(lines)]
    new_model = lines_one + lines_three
  
  with open(read_file, "w") as file:
    for line in new_model:
      file.write(line)

