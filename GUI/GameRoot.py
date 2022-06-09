from tkinter import *
from tkinter import messagebox

from Algorithms.Environment import Board
from GUI.MainMenu import MainMenu
from GUI.GameCanvas import GameCanvas


class ConnectFour(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('Connect Four')
        self.resizable(False, False)
        self.exitMainLoop = False
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.MainWindow = MainMenu(self)

        
        #self.yellowAgent = ...
        #self.redAgent = ...

    def createCanvas(self, canvasType):
        self.MainWindow.destroy()
        self.MainWindow = GameCanvas(self)

    def onClosing(self):
        self.exitMainLoop = True
