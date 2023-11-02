import random
from tkinter import *

def esy():
  global root
  root.destroy()
  exec("RockPapperSizoser/esy.py")
def hard():
  global root
  from RockPapperSizoser.hard import start; start()
  root.destroy()
root = Tk()
root.config(background= "black",cursor="none")

label1 = Label(root, text = "Rock Papper Sizoser\n \n Esy or Hard", fg = "white",bg = "black")

esy = Button(root, text = "Esy",command= esy,fg = "white",bg = "black")
hard = Button(root, text = "Hard",command= hard,fg = "white",bg = "black")

label1.grid(row= 0, column= 0, columnspan= 2)

esy.grid(row = 1, column= 0)
hard.grid(row = 1, column= 1)