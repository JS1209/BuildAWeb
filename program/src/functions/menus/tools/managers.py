import sys

from functions.menus.tools.checkers import *
from functions.menus.tools.writers import *
import os
import shutil

source = '../sourceFiles/'

# Collect and copy right files, creating a folder in builtSites by:
#   - Copying routers, middleware and jwt
#   - Copying models and migrations and:
#     - insert extra options (dob, nat, num) from sourceFiles/models/features.js (or maybe change to */features.json, not sure yet)
# (EXTRA) Check if features even exist
# (EXRTA) Insert features
# (EXTRA) Insert relations in routers, models and migrations


# build_login is the function that fixes all the files for the login system. We need routers, middleware, JWT, models and migrations.
# These files are only required when initializing the login, so they only need to get added once. Therefore, we can check if it already
# has been created, to prevent code from unwanted repetition.
def build_login(path_to_user):

  # JWT, middleware and routers don't need to get tweaked, we can just copy them. In pseudocode it says: if file not present -> make file
  if os.path.exists(path_to_user + "/backend/auth/jwt.js") == False:
    copy_files(source + 'backend/auth/jwt.js', path_to_user + '/backend/auth/jwt.js')
    if os.path.exists(path_to_user + '/backend/auth/middleware.js') == False:
      copy_files(source + 'backend/auth/middleware.js', path_to_user + '/backend/auth/middleware.js')
      if os.path.exists(path_to_user + '/backend/routers/auth.js') == False:
        copy_files(source + 'backend/routers/auth.js', path_to_user + '/backend/routers/auth.js')

  # For models we have to copy the files as well, we will tackle models and migrations seperately.
  # First copy the model, then check what extra's the user wanted (dob, nat, num). Get that attribute from a a list of attributes and
  # insert it in the model. To keep it simple, we add it as the second attribute, after id.
  if (os.path.exists(path_to_user + "/backend/models/user.js")) == False:
    copy_files(source + 'backend/models/user.js', path_to_user + 'backend/models/user.js')
    insert_attribute(source + 'backend/models/attributes.json', path_to_user + 'backend/models/user.js', "nationality")

  
# def delete_login(path_to_user):
#   shutil.rmtree(path_to_user + '/backend/auth/')
#   os.remove(path_to_user + '/backend/routers/auth.js')