import os
from tools.dialogs_inputs import *
from tools.menu_browser import *

# menu to add features, shows all available features to add
def add_features():
    dialog_add_feature_menu()
    menu_options_path = "menu_options/add_features_menu_options/"

    # show all available menu's, takes all menu.py files in menus folder and lists them
    menu_file_names = menu_option_displayer(menu_options_path)
    
    your_pick = input_menu_option_pick()

    # go back to main menu if instructed
    if your_pick == "main":
        import main_menu
    else:
        # open the menu that is closest to whatever the user inputted
        menu_caller(menu_options_path, menu_file_names, your_pick)







# run this menu when file is selected
add_features()