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
        self.canvasIsMainWindow = False

        self.MainWindow = MainMenu(self)

        
        #self.yellowAgent = ...
        #self.redAgent = ...

    def createCanvas(self, c):
        self.MainWindow.destroy()
        self.MainWindow = GameCanvas(self)
        self.MainWindow.canvasType = c
        self.canvasIsMainWindow = True

    def createMainMenu(self):
        pass
    def onClosing(self):
        self.exitMainLoop = True
