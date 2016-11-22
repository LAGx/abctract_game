import tkinter as tk
r = tk.Tk()

####screen
screen_mode = "full" #full normal test
SCREENSIZE = ((r.winfo_screenwidth(), r.winfo_screenheight()), (900,500),(400,400))
dialogSize = ((r.winfo_screenwidth(), r.winfo_screenheight()/6), (900,500/6),(400,400/6))

def currScreenSize():
    if screen_mode == "full":
        return SCREENSIZE[0]
    elif screen_mode == "normal":
        return SCREENSIZE[1]
    elif screen_mode == "test":
        return SCREENSIZE[2]
    else:
        print("Error screen_mode")

def currDialogSize(axis):
    if axis == "x":
        if screen_mode == "full":
            return dialogSize[0][0]
        elif screen_mode == "normal":
            return dialogSize[1][0]
        elif screen_mode == "test":
            return dialogSize[2][0]
    if axis == "y":
        if screen_mode == "full":
            return dialogSize[0][1]
        elif screen_mode == "normal":
            return dialogSize[1][1]
        elif screen_mode == "test":
            return dialogSize[2][1]


####colors
class Color:
    background = (5,20, 20)
    player = (10,170,170)
    text_dialog = (100, 255, 200)
    background_dialog = (10, 30,30)
####
