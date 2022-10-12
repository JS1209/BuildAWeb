# dialogs
###########################################################################

def dialog_welcome_msg():
    print("\n\n\n~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****")
    print("\nWelcome to the website builder v1.0 made by JS1209")
    print("This application is intended for personal use, so please don't do get me in trouble. Thanks, yours truly\n\n")
    print("------------------------------------------------------------------------------------------------\n")
    
def dialog_menu_option(x):
    no_extension = x.replace("_menu.py", "")
    no_space = no_extension.replace("_", " ")
    print("- " + no_space)
    return no_space

def dialog_main_menu():
    print("If you want to stop this program, at any time type STOP")
    print("If at any time you want to restart the program, type RESTART")
    print("If you want to return to previous menu's, type RETURN")
    print("If at any time you feel like spending money just for the sake of it, please contact me at jesje1209@live.nl \n")
    print("Feel free to enjoy :) \n")
    print("------------------------------------------------------------------------------------------------\n\n")
    print("\n\n~~~Main Menu~~~\n\n")
    print("Here are your options: ")

def dialog_add_feature_menu():
    print("\n\n~~~Add Features Menu~~~\n\n")
    print("Here are your options: ")


# inputs
###########################################################################

def input_menu_option_pick():
    print("(type 'main' to go back to main menu)")
    return input("\nWrite your pick down here: ")

def input_back_to_main_menu():
    return input("Do you want to go back to the main menu? y/n ")
