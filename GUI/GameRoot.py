from tkinter import *
from tkinter import messagebox

from Algorithms.Environment import Board


class ConnectFour(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('Connect Four')
        self.resizable(False, False)
        self.exitMainLoop = False

        #The game initially starts with a main menu, not a canvas, thus this is initially none.
        self.currentCanvas = None   

        self.Board = Board()
        #self.yellowAgent = ...
        #self.redAgent = ...


