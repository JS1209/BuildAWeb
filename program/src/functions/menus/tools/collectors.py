import sys
sys.path.append("..")
from functions.menus.tools.checkers import *
from functions.menus.tools.writers import *
import os
import shutil

backend_source = '../sourceFiles/'

def build_login(path_to_user):
  build(backend_source + 'backend/auth/jwt.js', path_to_user + '/backend/auth/jwt.js', '')
  build(backend_source + 'backend/auth/middleware.js', path_to_user + '/backend/auth/middleware.js', '')
  build(backend_source + 'backend/routers/auth.js', path_to_user + '/backend/routers/auth.js', '')

  
def delete_login(path_to_user):
  shutil.rmtree(path_to_user + '/backend/auth/')
  os.remove(path_to_user + '/backend/routers/auth.js')
  