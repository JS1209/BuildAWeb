import os
import sys
sys.path.append("..")
from functions.checks import *

def search_str(read_file, write_file, word):
  if word == '':
    get_whole_file(read_file, write_file)
  else:
    with open(read_file, 'r') as file:
      lines = file.readlines()
      for line in lines:
        if line.find(word) != -1:
          found = True
          get_function_by_brackets(read_file, write_file, lines.index(line))
          break

def get_whole_file(read_file, write_file):
  while True:
    with open(read_file, 'r') as file:
      for line in file:
        bedue = file.readline()
        write_line_to_file(write_file, line)
        write_line_to_file(write_file, bedue)
        if not bedue:
          break
      break

def get_function_by_brackets(read_file, write_file, line_number):
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
          break
        if line.find('}') != -1:
          x = x - line.count('}')
        if x == 0:
          break
      break

def append_line_to_file(write_file, line):
  with open(write_file, 'a') as file:
    file.write(line)

def write_line_to_file(write_file, line):
  os.makedirs(os.path.dirname(write_file), exist_ok=True)
  if os.path.exists(write_file):
    print("IT DOES")
    append_line_to_file(write_file, line)
  else:
    print("IT DOESNT")
    with open(write_file, 'w') as file:
      file.write(line)