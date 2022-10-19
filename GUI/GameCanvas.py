from tkinter import *
from tkinter import messagebox

from Backend.Environment import Board

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
        self.canvasType = None

        self.bind('<<Human-Turn>>', self.enableClicks)
        self.bind('<<AI-Turn>>', self.getAITurn)
        self.bind('<<Eval-Board>>', self.getEval)

    
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
    
    def enableClicks(self,e):
        self.focus()
        self.bind('<ButtonRelease-1>', self.getClicks)

    def getClicks(self, e):
        columnNo = -1
        color = -1
        if (e.x >= 0 and e.x < 160):
            columnNo = 0
        elif(e.x >= 160 and e.x < 256):
            columnNo = 1
        elif(e.x >= 256 and e.x < 352):
            columnNo = 2
        elif(e.x >= 352 and e.x < 448): 
            columnNo = 3
        elif(e.x >= 448 and e.x < 544):
            columnNo = 4
        elif(e.x >= 544 and e.x < 640):
            columnNo = 5
        elif(e.x >= 640 and e.x < 800):
            columnNo = 6
        
        if(self.currentTurn == 'Yellow'):
            color = 1
        else:
            color = 2
        
        piecePlaced = self.Board.addPiece(columnNo, color)
        
        #case 0 and 1: piece is placed and now it is AI turn
        if piecePlaced == True:
            self.generateEvaluateBoard()
            self.currentTurn = 'Yellow' if self.currentTurn == 'Red' else 'Red'
            if(self.canvasType == 0 or self.canvasType == 1):
                self.unbind('<ButtonRelease-1>')
                self.humanTurn = False



    def getAITurn(self, e):
        pass

    def getEval(self, e):
        print('hello, we get here 2')
        self.drawBoard()
        self.master.update_idletasks()
        #case 1: Show messagebox for draw for games that involve players
        if self.Board.boardIsFilled() and (self.canvasType!= 4 or self.canvasType != 5) and (not self.Board.checkWinner()):
            self.drawBoard()
            messagebox.showinfo('Draw', 'The game is drawn!')
            self.master.createMainMenu()
        #case 2: Show messagebox to indiciate game winner.
        elif self.Board.checkWinner() and (self.canvasType != 4 or self.canvasType != 5):
            self.drawBoard()
            winner = 'Yellow' if self.Board.getWinner() == 1 else 'Red'
            messagebox.showinfo('Winner', f'{winner} wins the game!')
            self.master.createMainMenu()
        

    def generateHumanTurn(self):
        self.event_generate('<<Human-Turn>>')
    
    def generateAITurn(self):
        self.event_generate('<<AI-Turn>>')
    
    def generateEvaluateBoard(self):
        self.event_generate('<<Eval-Board>>')
    
    
