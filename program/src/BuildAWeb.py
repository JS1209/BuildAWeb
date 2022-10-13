import sys

from functions.menus import *
from functions.tools.checkers import *
from functions.tools.utils import *
from functions.tools.managers import *
from functions.tools.writers import *


def log_menu(user_name, path_to_user):
  properties_file = '../../builtSites/' + user_name + '/properties.json'
  login_enabled = False
  nat_enabled = False
  dob_enabled = False
  num_enabled = False

  print("\n_________________________________________________________________________________________________________")
  print("_________________________________________THIS IS THE LOG MENU____________________________________________")
  print("_________________________________________________________________________________________________________")
  print('_________________________________________________________________________________________________________')
  print('STATUS::')
  with open('../../builtSites/' + user_name + '/properties.json', 'r') as file:
    lines = file.readlines()
    for line in lines:
      if line.find("LOGIN: 1") != -1:
        login_enabled = True
      elif line.find("NAT: 1") != -1:
        nat_enabled = True
      elif line.find("DOB: 1") != -1:
        dob_enabled = True
      elif line.find("NUM: 1") != -1:
        num_enabled = True
      print(line)
  print('_________________________________________________________________________________________________________')
  if login_enabled:
    print("Login system is enabled. Switching between enabling/disabling functionality can be done by typing the\n")
    print("specified commandsIt is also possible to disable the whole login system, by typing LOGIN: 0. Be carefull\n")
    print(" with this, as it deletes the loginsystem and preferences entirely. The next commands are available for\n")
    print("enabling/disabling:\n")
    print("- date of birth (DOB)")
    print("- Nationality (NAT)")
    print("- phonenumber (NUM)")
  else:
    print("Login system is disabled. To enable the login system type 'LOGIN'")

  while True:
    user_input = input('')

    if user_input.upper() == "STOP":
      print("Program will be terminated")
      sys.exit()
    elif user_input.upper() == "RESTART":
      print("Program will be restarted")
      start()
    elif user_input.upper() == "BACK":
      return 0
    elif user_input == '':
      print("I really need input broski, you can do it!")

    ### STATUS
    elif user_input.upper() == "STATUS":
      print('_______________________________________________________')
      print('STATUS::')
      with open(properties_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
          print(line)
      print('_______________________________________________________')

    ### SWITCH LOGIN
    elif user_input.upper() == "LOGIN":
      if login_enabled:
        print("! ! !WARNING: Disabling login system entirely! ! !")
        replace_line(properties_file, "LOGIN: 1", " -> LOGIN: 0\n")
        login_enabled = False
      else:
        print("! ! !WARNING: Enabling login system entirely! ! !")
        replace_line(properties_file, "LOGIN: 0", " -> LOGIN: 1\n")
        login_enabled = True

    ### SWITCH NATIONALITY
    elif user_input.upper() == "NAT":
      if nat_enabled:
        print("! ! !WARNING: Disabling nationality! ! !")
        replace_line(properties_file, "NAT: 1", "    - NAT: 0\n")
        nat_enabled = False
      else:
        print("! ! !WARNING: Enabling nationality! ! !")
        replace_line(properties_file, "NAT: 0", "    - NAT: 1\n")
        nat_enabled = True

    ### SWITCH DATE OF BIRTH
    elif user_input.upper() == "DOB":
      if nat_enabled:
        print("! ! !WARNING: Disabling nationality! ! !")
        replace_line(properties_file, "DOB: 1", "    - DOB: 0\n")
        dob_enabled = False
      else:
        print("! ! !WARNING: Enabling nationality! ! !")
        replace_line(properties_file, "DOB: 0", "    - DOB: 1\n")
        dob_enabled = True

    ### SWITCH PHONENUMBER
    elif user_input.upper() == "NUM":
      if nat_enabled:
        print("! ! !WARNING: Disabling nationality! ! !")
        replace_line(properties_file, "NUM: 1", "    - NUM: 0\n")
        num_enabled = False
      else:
        print("! ! !WARNING: Enabling nationality! ! !")
        replace_line(properties_file, "NUM: 0", "    - NUM: 1\n")
        num_enabled = True

    ### BUILD ACCORDING TO PROPERTIES
    elif user_input.upper() == "UPDATE":
      if login_enabled:
        build_login(path_to_user)

      
      


def start ():
  print("\n\n\n~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****~~~~````****")
  print("\nWelcome to the website builder v1.0 made by JS1209")
  print("This application is intended for personal use, so please don't do get me in trouble. Thanks, yours truly\n\n")
  print("------------------------------------------------------------------------------------------------\n")
  print("If you want to stop this program, at any time type STOP")
  print("If at any time you want to restart the program, type RESTART")
  print("If you want to return to previous menu's, type RETURN")
  print("If at any time you feel like spending money just for the sake of it, please contact me at jesje1209@live.nl \n")
  print("Feel free to enjoy :) \n")
  print("------------------------------------------------------------------------------------------------\n\n")
  user_name = input("What is your first name (must be one worded, only characters and numbers): ")
  path_to_user = '../../builtSites/' + user_name + '/'
  properties = path_to_user + 'properties.json'

  os.makedirs(os.path.dirname(path_to_user), exist_ok=True)
  initialize_properties(properties, user_name)
  # with open(properties, 'w') as file:
  #   file.write("NAME: " + user_name + "\n FEATURES: \n -> LOGIN: 0\n    - NAT: 0\n    - DOB: 0\n    - NUM: 0\n")

  while True:
    print("\n_________________________________________________________________________________________________________")
    print("______________________________________________Main Menu__________________________________________________")
    print("_________________________________________________________________________________________________________")
    print("Okay cool %s, let's start with the backend, which of the following features shall we start with:" %user_name)
    print("- User system for login/signup (type 'LOG')\n\n")
    user_input = input('')
    print('\n\n')
    if user_input.upper() == "STOP":
      print("Program will be terminated")
      return
    elif user_input.upper() == "RESTART":
      print("Program will be restarted")
      start()
    elif user_input == '':
      print("I really need input broski, you can do it!")
    elif user_input.upper() == "TEST":
      add_json()
    else:
      if user_input.upper() == "LOG":
        log_menu(user_name, path_to_user)
start()