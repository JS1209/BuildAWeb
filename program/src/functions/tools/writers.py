import os
import sys
from unittest.util import three_way_cmp
sys.path.append("..")
from functions.tools.checkers import *
from functions.tools.utils import *

# copy_files copies whole files, without checking if anything is double. This function is only called when
# absolutely sure certain directories/files are not yet present, for example when enabling login system.
# The check if a directory/file is present is done in the function that calls this one.
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



# ------------------------------------------------- FROM HERE ON I'M STILL BUSY REWRITING THE PROGRAM
# ------------------------------------------------- FUNCTIONS WORK, BUT I WILL CHANGE THEM A LOT!!!!!


def insert_attribute(read_file, write_file, name):
  asdf = read_file
  # with open(read_file, 'r') as r_file:
    # lines = r_file.readlines()
    # for line in lines:        
    #   if line.find(name):
    #     func = get_func(read_file, lines.index(line))
    #     print(func)

# def get_func(read_file, index):
#   x = 0
#   while True:
#     with open(read_file, 'r') as file:
#       for i in range(index):
#         next(file, None)
#       for line in file:
#         func = func.append(line)
#         if line.find('{') != -1:
#           x = x + line.count('{')
#         if line.find('}') != -1:
#           x = x - line.count('}')
#         if x == 0:
#           return func
#       return 1  


def build(read_file, write_file, word):
  with open(read_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      if line.find(word) != -1:
        insert_function_by_linenumber(read_file, write_file, lines.index(line))
        return 0
  return 1


def insert_function_by_linenumber(read_file, write_file, line_number):
  x = 0
  while True:
    with open(read_file, 'r') as file:
      for i in range(line_number):
        next(file, None)
      for line in file:
        append_line_to_file(write_file, line)
        if line.find('{') != -1:
          x = x + line.count('{')
        if x == 0:
          return 0
        if line.find('}') != -1:
          x = x - line.count('}')
        if x == 0:
          return 0
      return 1

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

def replace_line(write_file, old_line, new_line):
  with open(write_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      if line.find(old_line) != -1:
        lines[lines.index(line)] = new_line
  with open(write_file, 'w') as file:
    file.writelines(lines)
    return 0

