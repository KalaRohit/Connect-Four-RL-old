from tkinter import *
from tkinter import messagebox

from Algorithms.Environment import Board

class GameCanvas(Canvas):

    X1_CORDINATE = 64
    Y1_CORDINATE = 503

    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)
        self.backgroundImage = PhotoImage(file='./Assets/background.png')
        super().create_image(0,0, image=self.backgroundImage, anchor=NW)
        self.pack()
        
        self.Board = Board()
        self.currentTurn = 'Yellow'
        self.humanTurn = True

        self.bind('<<Human-Turn>>', self.enableClicks())
        self.bind('<<AI-Turn>>', self.getAITurn())
        self.bind('<<Eval-Board>>', self.getEval())

    
    def drawBoard(self):
        board = self.Board.currentBoard
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == Board.YELLOW): #case where it is yellow
                    y1 = self.Y1_CORDINATE - (96 *(i))
                    x1 = self.X1_CORDINATE + (96 * (j))
                    self.drawPiece(x1,y1,x1+95,y1+96, Board.YELLOW)
                elif(board[i][j] == 2): #case where it is red
                    y1 = self.Y1_CORDINATE - (96 *(i))
                    x1 = self.X1_CORDINATE + (96 * (j))
                    self.drawPiece(x1,y1,x1+95,y1+96, Board.RED)
    
    def drawPiece(self,x1,y1, x2, y2, pieceColor):
        color = 'Yellow' if pieceColor == Board.YELLOW else 'Red'
        self.create_oval(x1,y1,x2,y2, fill=color)
    
    def enableClicks(self, e):
        self.focus()
        self.bind('<<Button-Release-1>>', self.getClicks())

    def getClicks(self):
        column_no = -1
        color = -1
        if (e.x >= 0 and e.x < 160):
            column_no = 0
        elif(e.x >= 160 and e.x < 256):
            column_no = 1
        elif(e.x >= 256 and e.x < 352):
            column_no = 2
        elif(e.x >= 352 and e.x < 448): 
            column_no = 3
        elif(e.x >= 448 and e.x < 544):
            column_no = 4
        elif(e.x >= 544 and e.x < 640):
            column_no = 5
        elif(e.x >= 640 and e.x < 800):
            column_no = 6
        if(self.master.yellow_turn):
            color = 1
        else:
            color = 2

    def getAITurn(self):
        pass

    def getEval(self):
        pass

    def generateHumanTurn(self):
        self.event_generate('<<Human-Turn>>')
    
    def generateAITurn(self):
        self.event_generate('<<AI-Turn>>')
    
    def generateEvaluateBoard(self):
        self.event_generate('<<Eval-Board>')
    
