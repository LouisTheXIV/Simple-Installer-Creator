import os
import tkinter as tk
from tkinter import *

screen = tk.Tk()

screen.title("Just Another Mod Installer")
screen.geometry("800x600")
screen.iconbitmap("icon.ico")

def desktop():
    file1 = open('Mod/installer/shortcut.civ4installer', 'w')
    file1.write('1')
    file1.close()    

##welcome and mod name
Welcome = Label(screen, text="Welcome to a mod installer. Drop your Mod in the Mod folder to start!")
Welcome.config(font=('Italic',16))
Welcome.grid(sticky = S)
Label(screen, text="Name of your mod*", font=('Arial', 12)).grid()
mod = Entry(screen, width=50, fg='blue')
mod.grid()
##size
size_label = Label(screen, text="What size should the Installer window be?* EG: 800x600", font=('Arial',11))
size_label.grid(row=30,sticky=E)
size = Entry(screen, width=10, fg='blue')
size.grid(row=32,sticky=E)
##icon
icon_label = Label(screen, text="type the name of the icon file, type none if none", font=('Arial',11))
icon_label.grid(row=40,sticky=E)
icon = Entry(screen, width=10, fg='blue')
icon.grid(row=42,sticky=E)
##main message
mm_label = Label(screen, text="Main Message on Screen*", font=('Arial',11))
mm_label.grid(row=50,sticky=E)
mm = Entry(screen, width=12, fg='blue')
mm.grid(row=52,sticky=E)
##middle screen text
text_label = Label(screen, text="Message on Screen* EG: Choose the options below", font=('Arial',11))
text_label.grid(row=60,sticky=N)
text = Entry(screen, width=30, fg='blue')
text.grid(row=62,sticky=N)
##desktop shortcut
##Checkbutton(screen, text='Desktop Shortcut Option', command=desktop).grid(row=80,sticky=S)
##module 1
#Label(screen, text="put the exact name of the modules folder name in Assets/Modules", font=('Arial',12)).grid(row = 20, sticky = W)
m1l = Label(screen, text="Optional Module 1, if you don't want it type none", font=('Arial',12))
m1l.grid(row = 26, column = 0, sticky = W)
m1 = Entry(screen, width=15, fg='blue')
m1.grid(row = 28, column = 0, sticky = W)
##module 2
m2l = Label(screen, text="Optional Module 2", font=('Arial',12))
m2l.grid(row = 32, column = 0, sticky = W)
m2 = Entry(screen, width=15, fg='blue')
m2.grid(row = 35, column = 0, sticky = W)
##module 3
m3l = Label(screen, text="Optional Module 3", font=('Arial',12))
m3l.grid(row = 42, column = 0, sticky = W)
m3 = Entry(screen, width=15, fg='blue')
m3.grid(row = 45, column = 0, sticky = W)



## Installer Creator
def finish():
    file = open('Mod/installer/name.civ4installer', 'w')
    file.write(mod.get())
    file.close()
    file2 = open('Mod/installer/size.civ4installer', 'w')
    file2.write(size.get())
    file2.close()
    file3 = open('Mod/installer/icon.civ4installer', 'w')
    file3.write(icon.get())
    file3.close()
    file4 = open('Mod/installer/mm.civ4installer', 'w')
    file4.write(mm.get())
    file4.close()
    file5 = open('Mod/installer/text.civ4installer', 'w')
    file5.write(text.get())
    file5.close()
    file6 = open('Mod/installer/module1.civ4installer', 'w')
    file6.write(m1.get())
    file6.close()
    file7 = open('Mod/installer/module2.civ4installer', 'w')
    file7.write(m2.get())
    file7.close()
    file8 = open('Mod/installer/module3.civ4installer', 'w')
    file8.write(m3.get())
    file8.close()


finishbtn = Button(screen, text="Finish!", command=finish)
finishbtn.grid(row=100, column = 1)









screen.mainloop()
