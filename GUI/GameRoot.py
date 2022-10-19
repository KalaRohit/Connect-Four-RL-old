from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time

from Backend.Environment import Board
from Backend.BoardJSON import BoardJSON
from Backend.BoardJSONParser import Parser
from GUI.MainMenu import MainMenu
from GUI.GameCanvas import GameCanvas
from GUI.GameMenu import ConnectFourMenu


class ConnectFour(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('Connect Four')
        self.resizable(False, False)
        self.exitMainLoop = False
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.canvasIsMainWindow = False
        self.menu = ConnectFourMenu(self)

        self.MainWindow = MainMenu(self)

        
        #self.yellowAgent = ...
        #self.redAgent = ...

    def createCanvas(self, c):
        self.menu.enableMenuOptions()
        self.MainWindow.destroy()
        self.MainWindow = GameCanvas(self)
        self.MainWindow.canvasType = c
        self.canvasIsMainWindow = True

    def createMainMenu(self):
        self.canvasIsMainWindow = False
        self.MainWindow.pack_forget()
        self.MainWindow.destroy()
        self.MainWindow = MainMenu(self)
        self.MainWindow.pack()

    def onClosing(self):
        self.exitMainLoop = True
    
    def saveCurrentBoard(self):
        if self.canvasIsMainWindow:
            board = self.MainWindow.Board
            board.setGUICanvasType(self.MainWindow.canvasType)
            fileName = simpledialog.askstring('Save File', 'Enter file name:')
            if fileName != '':
                test = BoardJSON(board, fileName)
            else:
                messagebox.showerror('Error Saving', 'Invalid name for save file!')
                raise Exception('Invalid save file name!')
            print('Saving Complete...')
        else:
            messagebox.showerror('Error Saving', 'Tried to save without a playable board!')
            raise Exception('Tried to save without a playable board!')
    
    def loadBoard(self):
        self.canvasIsMainWindow = False
        p = Parser('testing')
        loadedBoard = p.parseFile()
        self.createCanvas(loadedBoard.guiCanvasType)  
        self.MainWindow.Board = loadedBoard
        print(type(self.MainWindow))
        self.MainWindow.generateEvaluateBoard()
        if self.MainWindow.Board.movesMade % 2 == 0:
            self.MainWindow.currentTurn = 'Yellow'
        else:
            self.MainWindow.currentTurn = 'Red'

        self.MainWindow.drawBoard()
        self.update_idletasks()