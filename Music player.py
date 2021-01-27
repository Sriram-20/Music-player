import pygame
from pygame import mixer
from tkinter import *
import os

#working function
def Playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("playing")
    mixer.music.play()

def pausesong():
    songstatus.set("paused")
    mixer.music.pause()
    

def resumesong():
    songstatus.set("resume")
    mixer.music.unpause()
    

def stopsong():
    songstatus.set("stopped")
    mixer.music.stop()


root = Tk()
root.title('Music player')

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")


#playlist
playlist = Listbox(root, selectmode = SINGLE, bg = "black", fg ="white", font= ('CinzelRegular', 15),width = 40)
playlist.grid(columnspan = 5)

os.chdir(r'D:\movies\Songs\English Songs')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text = "Play", command = Playsong)
playbtn.config(font = ('CinzelRegular', 20), bg = "white", fg = "DodgerBlue2", padx = 5, pady =5)
playbtn.grid(row = 1, column = 0)

pausebtn = Button(root, text= "Pause", command = pausesong)
pausebtn.config(font = ('CinzelRegular', 20), bg = "white", fg = "DodgerBlue2", padx =5, pady =5)
pausebtn.grid(row = 1, column = 1)

Resumebtn = Button(root, text = "Resume", command = resumesong)
Resumebtn.config(font = ('CinzelRegular', 20), bg = "white", fg = "DodgerBlue2", padx =5, pady =5)
Resumebtn.grid(row = 1, column = 2)

stopbtn =Button(root, text = "Stop", command = stopsong)
stopbtn.config(font = ('CinzelRegular', 20), bg = "white", fg = "DodgerBlue2", padx =5, pady =5)
stopbtn.grid(row = 1,column = 3)

mainloop()
