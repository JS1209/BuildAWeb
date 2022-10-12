import os
import sys
sys.path.append("..")
# from tools.managers import *

def check_presence_function(file_, word):
  if word != '':
    if os.path.exists(file_):
      with open(file_, 'r') as file:
        lines = file.readlines()
        for line in lines:
          if line.find(word) != -1:
            return True
  return False