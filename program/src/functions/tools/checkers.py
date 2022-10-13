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

# Checks at what line the code has to be placed in the model
def check_model_placement(path_to_user, model):
  start = False
  started = False
  index = -2
  x = 0
  with open(path_to_user + "backend/models/" + model + ".js", "r") as file:
    lines = file.readlines()

  for line in lines:
    if line.find(".init(") != -1:
      index = lines.index(line)
      start = True
    elif (line.find("{") != -1 or line.find("}") != -1) and start == True:
      if started == False:
        started = True
      x = x + line.count("{") - line.count("}")
    if x == 0 and start == True and started == True:
      return index
    index = index + 1
  return index
  
def check_migration_placement(path_to_user, migration):
  start = False
  started = False
  index = -2
  x = 0
  with open(path_to_user + "backend/migrations/" + migration + ".js", "r") as file:
    lines = file.readlines()

  for line in lines:
    if line.find("async up(queryInterface, Sequelize) {") != -1:
      index = lines.index(line)
      start = True
    elif (line.find("{") != -1 or line.find("}") != -1) and start == True:
      if started == False:
        started = True
      x = x + line.count("{") - line.count("}")
    if x == 0 and start == True and started == True:
      return index
    index = index + 1
  return index
  
def check_if_att_in_model(path_to_user, model, att):
  with open(path_to_user + "backend/models/" + model + ".js", "r") as file:
    lines = file.readlines()
    for line in lines:
      if line.find(att) != -1:
        return 0
  return 1


# def check_migration_placement():
#   asdf = "asdf"