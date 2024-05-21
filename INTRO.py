from tkinter import * 
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame  
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1500x750")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("orb.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("Startup2.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1500,750))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.03)
    root.destroy()

play_gif()
root.mainloop()