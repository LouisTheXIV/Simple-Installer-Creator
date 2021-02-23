import tkinter as tk
from tkinter import *
import os
import shutil

haveicon = False

title1 = open('installer/name.civ4installer', 'r')
if title1.mode == 'r':
    title = title1.read()
size1 = open('installer/size.civ4installer', 'r')
if size1.mode == 'r':
    size = size1.read()
icon1 = open('installer/icon.civ4installer', 'r')
if icon1.mode == 'r':
    global icon
    icon = icon1.read()
    if icon == 'none':
        pass
    else:
        haveicon = True
mm1 = open('installer/mm.civ4installer', 'r')
if mm1.mode == 'r':
    mm = mm1.read()
text1 = open('installer/text.civ4installer', 'r')
if text1.mode == 'r':
    text = text1.read()
module11 = open('installer/module1.civ4installer', 'r')
if module11.mode == 'r':
    module1 = module11.read()
module22 = open('installer/module2.civ4installer', 'r')
if module22.mode == 'r':
    module2 = module22.read()
module33 = open('installer/module3.civ4installer', 'r')
if module33.mode == 'r':
    module3 = module33.read()

def module1remove():
    modpath1 = f"installer/{title}/Assets/Modules/{module1}"
    shutil.rmtree(modpath1)
def module2remove():
    modpath2 = f"installer/{title}/Assets/Modules/{module2}"
    shutil.rmtree(modpath2)
def module3remove():
    modpath3 = f"installer/{title}/Assets/Modules/{module3}"
    shutil.rmtree(modpath3)

screen = tk.Tk()
screen.title(f"{title}")
screen.geometry(f"{size}")
if haveicon == True:
    screen.iconbitmap(icon)
else:
    pass

mm = Label(screen, text=f"{mm}")
mm.config(font=('Italic',16))
mm.grid(row = 5, sticky=S)
text = Label(screen, text=f"{text}")
text.config(font=('Arial', 12))
text.grid(row = 15, sticky=S)
Label(screen, text="Optional Modules, click the checkbox to remove them:", font=('Italic',11)).grid(row = 19, sticky = W)
if module1 == "none":
    pass
else:
    Checkbutton(screen, text=module1, command=module1remove).grid(row = 23, sticky = W)
if module2 == "none":
    pass
else:
    Checkbutton(screen, text=module2, command=module2remove).grid(row = 26, sticky = W)
if module3 == "none":
    pass
else:
    Checkbutton(screen, text=module3, command=module3remove).grid(row = 29, sticky = W)

Label(screen, text="Path to your Mods folder:", font=('Arial',11)).grid(row = 25, column=2, sticky = E)
global mod_folder
mod_folder = StringVar()
path_to_civ = Entry(screen, width=25, textvariable = mod_folder).grid(row = 26, column=2, sticky = E)



def finish():
    mod_path = f"installer/{title}"
    mods_folder = mod_folder.get()
    shutil.move(mod_path, mods_folder)  


Button(screen, text="Finish", font=('Arial','11'), command=finish).grid(row = 40, column=2, sticky = E)










