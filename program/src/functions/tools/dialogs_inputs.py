# dialogs
###########################################################################

from pprint import PrettyPrinter, pprint
from time import sleep
import json


def dialog_welcome_msg():
    print("\n\n\n~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****")
    print("\nWelcome to the website builder v1.0 made by JS1209 & Atubak")
    print("This application is intended for personal use, so please don't do get me in trouble. Thanks, yours truly\n\n")
    print("If you want to stop this program, at any time type STOP")
    print("If at any time you want to restart the program, type RESTART")
    print("If you want to return to previous menu's, type RETURN")
    print("If at any time you feel like spending money just for the sake of it, please contact me at jesje1209@live.nl \n")
    print("Feel free to enjoy :) \n")
    print("------------------------------------------------------------------------------------------------\n\n")
    print("------------------------------------------------------------------------------------------------\n")
    
def dialog_welcome_back_msg(username):
    print("\nWelcome Back %s!\n" %username)    

def dialog_menu_option(x):
    # take out the _menu or _feature suffix and insert spaces
    # crude way to check for both menu and feature, will come back later for a better solution
    no_extension = x.replace("_menu.py", "").replace("_feature.py", "")
    no_space = no_extension.replace("_", " ")
    print("- " + no_space)
    return no_space

def dialog_show_json(feature_name, username):
    file = open("../../builtSites/%s/properties.json" % username)
    data = json.dumps(json.load(file)["Systems"][feature_name])
    print("this feature: \n(0 means the feature is not installed, 1 means it is)\n\n" + data.replace(",", ",\n") + "\n\n")



def dialog_here_options():
    print("Here are your options: ")

def dialog_main_menu():
    print("\n\n~~~Main Menu~~~\n\n")
    sleep(2)
    

def dialog_add_feature_menu():
    print("\n\n~~~Add Features Menu~~~\n\n")
    sleep(2)
    

def dialog_remove_feature_menu():
    print("\n\n~~~Add Features Menu~~~\n\n")
    sleep(2)
    

def dialog_user_menu():
    print("\n\n~~~User Menu~~~\n\n")
    sleep(2)
    

def dialog_login_menu():
    print("\n\n~~~Login Menu~~~\n\nYou will need to install the base feature before you can install any extra's\n")
    sleep(2)
    

def dialog_login_feature():
    print("\n\n!!!(un)installed Login system!!!\n\n")
    sleep(2)

# inputs
###########################################################################

def input_menu_option_pick():
    return input("\nWrite your pick down here: ")

def input_back_to_main_menu():
    return input("Do you want to go back to the main menu? y/n ")

def input_username():
    return input("What's your name?")