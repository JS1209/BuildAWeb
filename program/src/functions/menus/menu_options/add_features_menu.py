import os

from functions.tools.dialogs_inputs import *
from functions.tools.menu_browser import *
from functions.menus.main_menu import *
from functions.tools.managers import *

# menu to add features, shows all available features to add
def add_features_menu(username):
    dialog_add_feature_menu()
    dialog_here_options()
    menu_options_path = "functions/menus/menu_options/add_features_menu_options/"

    # show all available menu's, takes all menu.py files in menus folder and lists them
    menu_file_names = menu_option_displayer(menu_options_path)
    
    your_pick = input_menu_option_pick()

    # go back to main menu if instructed
    if your_pick == "main" or your_pick == "RETURN":
       return None
    else:
        return {"menu_options_path": menu_options_path, "menu_file_names": menu_file_names, "your_pick": your_pick}

    




