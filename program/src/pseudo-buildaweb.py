# this file is just a placeholder for buildaweb which will manage the flow of the app 

from subprocess import call
from functions.menus.main_menu import *
from functions.menus.tools.dialogs_inputs import *


def flow_manager(chosen_menu):
    if chosen_menu == main_menu:
        dialog_welcome_msg()


    # passed menu functions will return a dictionary with menu_options_path, menu_file_names, your_pick that lead to the next menu 
    picked_menu_info = chosen_menu()

    # if there is no new menu to show, go back to main
    if picked_menu_info is None:
        return flow_manager(main_menu)
    
    # open the menu that is closest to whatever the user inputted
    called_menu = menu_caller(picked_menu_info["menu_options_path"], picked_menu_info["menu_file_names"], picked_menu_info["your_pick"])


    flow_manager(called_menu)

flow_manager(main_menu)