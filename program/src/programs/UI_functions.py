import sys
sys.path.append("..")
from functions.functionCopying import *
from functions.checks import *
import pathlib

backend_source = '/home/user/code/BuildAWeb/program/sourceFiles/'

def update_tasks(user_name, line):
  with open('/home/user/code/BuildAWeb/builtSites/' + user_name + '/tasks.txt', 'a') as file:
    file.write(line)
    return 0
  return 1

def build_login(path_to_user, user_name):
  with open('/home/user/code/BuildAWeb/builtSites/' + user_name + '/tasks.txt', 'a') as file:
    if build(backend_source + 'backend/auth/jwt.js', path_to_user + '/backend/auth/jwt.js', '') == 0:
      file.write("    * JWT: 1\n")
    else:
      file.write("    * JWT: 0\n")      
    if build(backend_source + 'backend/auth/middleware.js', path_to_user + '/backend/auth/middleware.js', '') == 0:
      file.write("    * MiddleWare: 1\n")
    else:
      file.write("    * MiddleWare: 0\n")
    if build(backend_source + 'backend/routers/auth.js', path_to_user + '/backend/routers/auth.js', '') == 0:
      file.write("    * Routers: 1\n")
    else:
      file.write("    * Routers: 0\n")
  
def build_model(path_to_user, user_name, options):
  