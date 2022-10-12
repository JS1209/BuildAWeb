import os

from tools.dialogs_inputs import *

# starting menu, shows welcome message and asks for user, initial options like adding/removing feats
def main_menu(): 
    dialog_main_menu()
    pickable_options = []
    menu_file_names = []
    
    # show all available menu's, takes all menu.py files in menus folder and lists them
    whole_dir = os.listdir()
    for data in whole_dir:
        # exclude the menu were currently in
        if data == "main_menu.py":
            continue

        if data.endswith("_menu.py"):
            # add filenames to list
            menu_file_names.append(data)

            # prints files as options to look better for user and adds those strings to pickable_options
            pickable_options.append(dialog_menu_option(data))

    print(pickable_options)
    your_pick = input_main_menu()

    # open the menu that is closest to whatever the user inputted
    for file_name in menu_file_names:
        if your_pick in file_name:
            # give user feedback as to what they chose
            dialog_menu_option(file_name)
            
            # call the corresponding menu
            importable_file_name = file_name.replace(".py", "")
            exec("import %s" % importable_file_name)


    
    


main_menu()