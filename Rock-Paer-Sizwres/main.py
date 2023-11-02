import random
from tkinter import * ; from tkinter import messagebox
conputer = 0
user = 0

def logic():
  global userchoise,user,conputer,lable3,lable4
  options = ["rock","papper","seisers"]
  computerschoise = random.choice(options)
  
  if computerschoise == userchoise:
    info ="Drew \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
    messagebox.showinfo("Results",info)
    
    print ("drew")
    print ("mine:",computerschoise)
    print ("yours:",userchoise)
  else:
    if computerschoise =="papper" and userchoise != "seisers":
      info ="Lose \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info)
      
      conputer = conputer +1 
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("computer")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
    elif userchoise =="papper" and computerschoise != "seisers":
      info ="Win \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info) 
      
      user = user +1 
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("user")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
    elif computerschoise =="rock" and userchoise != "papper":
      info ="Lose \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info)
      
      conputer =conputer = conputer +1
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("computer")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
    elif userchoise =="rock" and computerschoise != "papper":
      info ="Win \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info)
      
      user = user+ 1
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("user")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
    elif computerschoise =="seisers" and userchoise != "rock":
      info ="Lose \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info)  
      
      conputer =conputer = conputer +1
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("computer")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
    elif userchoise =="seisers" and computerschoise != "rock":
      info ="Win \nComputer: "+str(computerschoise)+"\nYours: "+str(userchoise)
      messagebox.showinfo("Results",info)  
      
      user =user+ 1
      lable4.config(text = "Conputer: " + str(conputer))
      lable3.config(text = "User: " + str(user))
      
      print ("user")
      print ("mine:",computerschoise)
      print ("yours:",userchoise)
      
    print ("---------------------------------------------------Restart---------------------------------------------------")
    print ()

def rock():
  global userchoise
  userchoise = "rock"
  logic()
def papper():
  global userchoise
  userchoise = "papper"
  logic()
def sisors():
  global userchoise
  userchoise = "seisers"
  logic()

root = Tk()
root.config(background="black",cursor="none")
    
rockIng =   PhotoImage(file = "RockPapperSizoser/rock.png")
papperIng = PhotoImage(file = "RockPapperSizoser/papper.png")
sisorsIng = PhotoImage(file = "RockPapperSizoser/sisors.png")
    
lable1 = Label(root,text ="Rock Papper Sizoser",font=('Helvetica bold', 26),bg="black",fg="white")
    
rock   = Button(root, image=  rockIng, command= rock  , height = 450, width = 300,bg = "black")
papper = Button(root, image=papperIng, command= papper, height = 450, width = 300,bg = "black")
sisors = Button(root, image=sisorsIng, command= sisors, height = 450, width = 300,bg = "black")
    
lable2 = Label(root, text = "Score", bg = "black", fg = "white",font=('Helvetica bold', 26))
lable3 = Label(root, text = "User: " + str(user), bg = "black", fg = "white",font=('Helvetica bold', 26))
lable4 = Label(root, text = "Conputer: " + str(conputer), bg = "black", fg = "white",font=('Helvetica bold', 26))
    
lable1.grid(row = 0,column= 0, columnspan = 3)
rock.grid(row = 1, column= 0)
papper.grid(row= 1, column= 1)
sisors.grid(row = 1, column=2)
    
lable2.grid(row = 2, column= 0)
lable3.grid(row = 2, column= 1)
lable4.grid(row = 2, column = 2)