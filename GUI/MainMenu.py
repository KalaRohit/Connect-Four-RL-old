from tkinter import *
from tkinter import messagebox


class MainMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)
        self.createMenu()
        self.pack()
        
    def createMenu(self):
        Button(self, text='Start a new game as yellow', width= 30,command=self.setUpYellowBoard).pack()
        Button(self, width= 30, command=self.setUpRedBoard, text='Start a new game as red').pack()
        Button(self, width= 30,command=self.setAIBoard, text='Spectate a game between AI').pack()
        Button(self, width= 30,text='Local Multiplayer Game', command=self.setUpMPBoard).pack()
    
    def setUpYellowBoard(self):
        self.master.createCanvas(0)
    
    def setUpRedBoard(self):
        self.master.createCanvas(1)

    def setAIBoard(self):
        self.master.createCanvas(2)
    
    def setUpMPBoard(self):
        self.master.createCanvas(3)
    
    def setUpTrainRedBoard(self):
        self.master.createCanvas(5)

    def setUpTrainYellowBoard(self):
        self.master.createCanvas(4)
