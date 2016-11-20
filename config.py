import tkinter as tk
r = tk.Tk()

####screen
screen_mode = "full" #full normal test
SCREENSIZE = ((r.winfo_screenwidth(), r.winfo_screenheight()), (900,500),(400,400))

def currScreenSize():
    if screen_mode == "full":
        return SCREENSIZE[0]
    elif screen_mode == "normal":
        return SCREENSIZE[1]
    elif screen_mode == "test":
        return SCREENSIZE[2]
    else:
        print("Error screen_mode")

####colors
background = (5,20, 20)
lights_1 = (10,170,170)
lights_2 = (170,10,170)




####
