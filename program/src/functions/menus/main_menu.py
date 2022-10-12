import os

from tools.dialogs_inputs import *
from tools.menu_browser import *

# starting menu, shows welcome message and asks for user, initial options like adding/removing feats
def main_menu(): 
    dialog_main_menu()
    menu_options_path = "menu_options/"
    
    # show all available menu's, takes all menu.py files in menus folder and lists them
    menu_file_names = menu_option_displayer(menu_options_path)
    
    your_pick = input_menu_option_pick()

    # open the menu that is closest to whatever the user inputted
    menu_caller(menu_options_path, menu_file_names, your_pick)


    
    

# run this menu when file is selected
main_menu()