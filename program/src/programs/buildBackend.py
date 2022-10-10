import sys
sys.path.append("..")
from functions.functionCopying import *
import pathlib

def start ():
  print("Welcome to the website builder v1.0 made by JS1209 \n")
  print("If you want to stop this program, at any time type 'STOP' \n")
  print("------------------------------------------------------------------------------------------------")
  print("This application is intended for personal use, please don't do any dumb shit with this, thanks, yours truly")
  print("------------------------------------------------------------------------------------------------")
  print("Lets start with the backend, which of the following features do you want:")
  print("login, signup, me")

  while True:
    user_input = input("")
    if user_input.upper() == "STOP":
      break
    if user_input == "":
      print("I really need input, you can do it!")
    if user_input.upper() == "LOGIN":
      search_str(r'/home/user/code/BuildAWeb/program/sourceFiles/backend/auth/jwt.js', '/home/user/code/BuildAWeb/builtSites/asdf/backend/auth/jwt.js', '')
      break

  # - Make a directory withing "builtSites" (at the root of this project) with all necessary features
  # - End program

start()