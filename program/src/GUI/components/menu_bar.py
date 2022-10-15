from tkinter import *
from tkinter import Menu

# En hier werkt het niet meer. Ik heb hier letterlijk alle mogelijke combinaties
# van imports geprobeerd, inclusief __init__.py files, sys.path.append("..") en
# van autocomplete gebruik gemaakt, maar het wil maar niet werken.....
from GUI.backend_page import *

def menu_bar(window):
  menubar = Menu(window)

  file_menu = Menu(menubar, tearoff=0)
  file_menu.add_command(label='New Web')

  web_menu = Menu(menubar, tearoff=0)
  web_menu.add_command(label='Systems')
  web_menu.add_command(label='Properties')
  web_menu.add_command(label='Features')
  web_menu.add_separator()

  sub_menu = Menu(web_menu, tearoff=0)

  web_menu.add_cascade(label="Build", menu=sub_menu)

  sub_menu.add_command(label="Backend", command=backend_page())
  sub_menu.add_command(label="Frontend")

  menubar.add_cascade(label='File', menu=file_menu)
  menubar.add_cascade(label='My Web', menu=web_menu)
  return menubar

# Hoi Sven, ik hoop dat je dit leest :)
# Dit werkt allemaal niet, maar ik wil backend_page() wel kunnen aanroepen hier
# omdat het onderdeel is van de menubar
# def navigate_backend():
  # backend_page()
  # backend_page.backend_page()
  # GUI.backend_page.backend_page()