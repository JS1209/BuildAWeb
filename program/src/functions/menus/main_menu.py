import os

from tools.dialogs import *

# starting menu, shows welcome message and asks for user, initial options like adding/removing feats
def main_menu(): 
    dialog_main_menu()
    
    pickable_options = []
    # show all available menu's, takes all menu.py files in menus folder and lists them
    whole_dir = os.listdir()
    for x in whole_dir:
        # exclude the menu were currently in
        if x == "main_menu.py":
            continue

        if x.endswith("_menu.py"):
            # add valid menus to list
            pickable_options.append(x)

            # format filenames to look better for user
            no_extension = x.replace("_menu.py", "")
            no_space = no_extension.replace("_", " ")
            print("- " + no_space)

    print(pickable_options)

main_menu()