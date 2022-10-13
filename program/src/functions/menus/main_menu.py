import os

from functions.menus.tools.dialogs_inputs import *
from functions.menus.tools.menu_browser import *

# starting menu, shows welcome message and asks for user, initial options like adding/removing feats
def main_menu(): 
    dialog_main_menu()
    menu_options_path = "functions/menus/menu_options/"
    
    # show all available menu's, takes all menu.py files in menus folder and lists them
    menu_file_names = menu_option_displayer(menu_options_path)
    
    your_pick = input_menu_option_pick()

    return {"menu_options_path": menu_options_path, "menu_file_names": menu_file_names, "your_pick": your_pick}
