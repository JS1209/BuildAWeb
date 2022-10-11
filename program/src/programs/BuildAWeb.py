import sys
sys.path.append("..")
from functions.functionCopying import *
from functions.checks import *
from programs.UI_functions import *
import pathlib


def log_menu(user_name, path_to_user):
  print("\n_________________________________________________________________________________________________________")
  print("_________________________________________THIS IS THE LOG MENU____________________________________________")
  print("_________________________________________________________________________________________________________")
  print("Let's get started with the backend of the login system. This is a system where your users can log in with \n"\
        "their email and password, but you might want to have some extra functionality for a personal page for example. \n" \
        "So what kind of extra credentials do you want the user to have (name, email and password already provided): \n")
  print("- no extra's (NOT)")
  print("- date of birth (DOB)")
  print("- Nationality (NAT)")
  print("- phonenumber (NUM)")

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
    else:
      with open('/home/user/code/BuildAWeb/builtSites/' + user_name + '/tasks.txt', 'a') as file:
          file.write(" -> Login: 1\n")
      if user_input.upper() == 'NOT':
        print("No extra's will be added.")
        build_login(path_to_user, user_name)
        return 0
      elif user_input.upper() == "NAT":
        print("The Nationality will be added")
        update_tasks(user_name, '     - NAT: 1\n')
      elif user_input.upper() == "DOB":
        print("Date of birth will be added")
        update_tasks(user_name, '     - NAT: 1\n')
      elif user_input.upper() == "NUM":
        print("Phonenumber will be added")
        update_tasks(user_name, '     - NUM: 1\n')
  


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

  os.makedirs(os.path.dirname('/home/user/code/BuildAWeb/builtSites/' + user_name + '/'), exist_ok=True)
  with open('/home/user/code/BuildAWeb/builtSites/' + user_name + '/tasks.txt', 'w') as file:
    file.write("NAME: %s \n FEATURES: \n" %user_name)
  path_to_user = '/home/user/code/BuildAWeb/builtSites/' + user_name

  while True:
    print("\n_________________________________________________________________________________________________________")
    print("______________________________________________Main Menu__________________________________________________")
    print("_________________________________________________________________________________________________________")
    print("Okay cool %s, let's start with the backend, which of the following features shall we start with:" %user_name)
    print("- User system for login/signup (type 'LOG')")
    user_input = input('')
    if user_input.upper() == "STOP":
      print("Program will be terminated")
      return
    elif user_input.upper() == "RESTART":
      print("Program will be restarted")
      start()
    elif user_input == '':
      print("I really need input broski, you can do it!")
    else:
      if user_input.upper() == "LOG" and (check_presence_function(path_to_user + '/tasks.txt', "Login: 1") == False):
        log_menu(user_name, path_to_user)
      elif user_input.upper() == "LOG" and (check_presence_function(path_to_user + '/tasks.txt', "Login: 1") == True):
        print("\n\n-----------> You already got a login system in your backend")

  # - Make a directory withing "builtSites" (at the root of this project) with all necessary features
  # - End program
start()