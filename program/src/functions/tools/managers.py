import sys

from functions.tools.checkers import *
from functions.tools.writers import *
from functions.tools.utils import *
import os
import shutil

source = '../sourceFiles/'


def add_mod_mig(path_to_user, model):
  if os.path.exists(path_to_user + "/backend/models/" + model + ".js") == False:
    copy_files(source + 'backend/models/' + model + '.js', path_to_user + '/backend/models/' + model + '.js')
  if os.path.exists(path_to_user + "/backend/migrations/" + model + ".js") == False:
    copy_files(source + 'backend/migrations/1-create-' + model + '.js', path_to_user + '/backend/migrations/1-create-' + model + '.js')

def apply_feat_to_mod_mig(path_to_user, system):
  prop_file = path_to_user + 'properties.json'
  model = json_value_by_key_middle(prop_file, "Models", system)
  for mod in model:
    features_dict = json_value_by_key_middle(prop_file, "Systems", system)
    enabled_features = []
    for key in features_dict:
      if features_dict[key] == 1 and key != 'Enabled':
        enabled_features.append(key)

    # We load the necessary lines to be added in arrays, and insert them later in the right spot
    feature_lines_for_models = []
    feature_lines_for_migrations = []
    for feat in enabled_features:
      feature_lines_for_models.append("      " + json_value_by_key_top(source + 'backend/models/attributes.json', feat) + "\n")
      feature_lines_for_migrations.append("      " + json_value_by_key_top(source + 'backend/migrations/attributes.json', feat) + "\n")

    # Index of placement in file
    model_line = check_model_placement(path_to_user, mod)
    migration_line = check_migration_placement(path_to_user, "1-create-" + mod)

    # Insert lines in file, after checking if it is already in the file
    for feat in feature_lines_for_models:
      if check_if_att_in_model(path_to_user, mod, feat) == 1:
        insert_lines_in_file_by_index(path_to_user + 'backend/models/'+ mod + '.js', feat, model_line)
    
    for featt in feature_lines_for_migrations:
      if check_if_att_in_migration(path_to_user, "1-create-" + mod + ".js", featt) == 1:
        insert_lines_in_file_by_index(path_to_user + "backend/migrations/1-create-" + mod + ".js", featt, migration_line )

def build_system(path_to_user, system):

  add_mod_mig(path_to_user, system)
  # add_routers(path_to_user, system)
  apply_feat_to_mod_mig(path_to_user, system)

def add_routers(path_to_user, system):
  asdf = "asdf"

# Since login needs a jwt and middleware, it's build as a separate function
def build_login(path_to_user):
  if os.path.exists(path_to_user + "/backend/auth/jwt.js") == False:
    copy_files(source + 'backend/auth/jwt.js', path_to_user + '/backend/auth/jwt.js')
  if os.path.exists(path_to_user + '/backend/auth/middleware.js') == False:
    copy_files(source + 'backend/auth/middleware.js', path_to_user + '/backend/auth/middleware.js')
  if os.path.exists(path_to_user + '/backend/routers/auth.js') == False:
    copy_files(source + 'backend/routers/auth.js', path_to_user + '/backend/routers/auth.js')
  add_mod_mig(path_to_user, "user")
  apply_feat_to_mod_mig(path_to_user, "user", "Login")

