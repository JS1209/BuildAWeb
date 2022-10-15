from tkinter import *
from tkinter import Menu

from GUI.backend_page import *
from GUI.components.menu_bar import *

window = Tk()
window.geometry("800x400")
window.title("Build A Web - JS1209")
window.config(menu=menu_bar(window))
window.mainloop()