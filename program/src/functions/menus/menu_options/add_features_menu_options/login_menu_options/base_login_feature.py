from functions.tools.managers import build_login
from functions.tools.dialogs_inputs import dialog_login_feature

# builds the initial login system without any extra's

def base_login_feature(username):
    path_to_user = "../../builtSites/" + username
    dialog_login_feature()
    build_login(path_to_user)

    return None