# this file is just a placeholder for buildaweb which will manage the flow of the app 

from subprocess import call
from functions.menus.main_menu import *
from functions.tools.dialogs_inputs import *
from functions.tools.checkers import check_presence_function
from functions.tools.utils import initialize_properties


user = input_username()
path_to_user = '../../builtSites/' + user + '/'
properties = path_to_user + 'properties.json'

def flow_manager(chosen_menu):

    # passed menu functions will return a dictionary with menu_options_path, menu_file_names, your_pick that lead to the next menu 
    picked_menu_info = chosen_menu(user)

    
    # if user typed main, pickedmenuinfo will be None, go back to main
    if picked_menu_info is None:
        return flow_manager(main_menu)
    
    # open the menu or call the feature that is closest to whatever the user inputted
    called_menu = menu_caller(picked_menu_info["menu_options_path"], picked_menu_info["menu_file_names"], picked_menu_info["your_pick"])

    flow_manager(called_menu)

#####################################


dialog_welcome_msg()

# check for a properties.json with this name, otherwise build a new folder with .json
if check_presence_function(properties, "Datetime"):
    dialog_welcome_back_msg(user)
else:
    properties = path_to_user + 'properties.json'

    os.makedirs(os.path.dirname(path_to_user), exist_ok=True)
    initialize_properties(properties, user)


flow_manager(main_menu)