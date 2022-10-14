import importlib
import os
from functions.tools.dialogs_inputs import *


# takes all menu options that go to submenus and display them in terminal
def menu_option_displayer(path_of_options_menu):
    menu_file_names = []

    # show all available menu's, takes all menu.py files in menus folder and lists them
    options_folder = os.listdir(path_of_options_menu)
    for data in options_folder:
        
        # if there's more menus, add them to the options
        if data.endswith("_menu.py") or data.endswith("_feature.py"):
            # add filenames to list
            menu_file_names.append(data)

            # prints files as options to look better for user and adds those strings to pickable_options
            # pickable_options.append(dialog_menu_option(data))
            dialog_menu_option(data)


    return menu_file_names

# takes the user's pick, file names for menu options and user's picked option, then calls the chosen menu function
def menu_caller(path_of_options_menu, menu_files, user_input):
    for file_name in menu_files:
        if user_input in file_name:
            # give user feedback as to what they chose
            dialog_menu_option(file_name)
            
            # call the corresponding menu
            importable_file_name = file_name.replace(".py", "")
            
            chosen_menu = importlib.import_module(path_of_options_menu.replace("/", ".") + importable_file_name)
            return getattr(chosen_menu, importable_file_name)