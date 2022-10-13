import sys

from functions.tools.checkers import *
from functions.tools.writers import *
from functions.tools.utils import *
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

  if (os.path.exists(path_to_user + "/backend/migrations/1-create-user.js")) == False:
    copy_files(source + 'backend/migrations/1-create-user.js', path_to_user + 'backend/migrations/1-create-user.js')

  # Now we need to apply all the extra attributes. All the enabled attributes are added to an array,
  # where we loop over and per attribute we add the necessary lines to the files.
  prop_file = path_to_user + 'properties.json'
  features_dict = json_value_by_key_middle(prop_file, "Systems", "Login")
  enabled_features = []
  for key in features_dict:
    if features_dict[key] == 1 and key != 'Enabled':
      enabled_features.append(key)

  # We load the necessary lines to be added in arrays, and insert them later in the right spot
  feature_lines_for_models = []
  feature_lines_for_migrations = []
  for feat in enabled_features:
    feature_lines_for_models.append("      " + json_value_by_key_top(source + 'backend/models/attributes.json', feat) + "\n")
    feature_lines_for_migrations.append("       " + json_value_by_key_top(source + 'backend/migrations/attributes.json', feat) + "\n")

  model_line = check_model_placement(path_to_user, "user")
  migration_line = check_migration_placement(path_to_user, "1-create-user")

  for feat in feature_lines_for_models:
    print(feat)
    if check_if_att_in_model(path_to_user, "user", feat) == 1:
      insert_lines_in_file_by_index(path_to_user + 'backend/models/user.js', feat, model_line)


  # Now we check for the right place to insert it and then call the writers that right the function
