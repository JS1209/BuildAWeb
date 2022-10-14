import os

from functions.tools.dialogs_inputs import *
from functions.tools.menu_browser import *
from functions.menus.main_menu import *



# menu to add a login system, shows all SUBfeatures available to add
def login_menu(username):
    dialog_login_menu()
    dialog_show_json("Login", username)
    dialog_here_options()

    menu_options_path = "functions/menus/menu_options/add_features_menu_options/login_menu_options/"

    # show all available menu's, takes all menu.py files in menus folder and lists them
    menu_file_names = menu_option_displayer(menu_options_path)
    
    your_pick = input_menu_option_pick()

    # go back to main menu if instructed
    if your_pick == "main":
       return None
    else:
        return {"menu_options_path": menu_options_path, "menu_file_names": menu_file_names, "your_pick": your_pick}



