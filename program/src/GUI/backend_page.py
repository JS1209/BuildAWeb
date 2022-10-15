from tkinter import *
from tkinter import Menu

def backend_page(window):
  page1text = Label(window, text="This is page 1")
  page2text = Label(window, text="This is page 2")
  page2text.pack_forget()
  page1text.pack()