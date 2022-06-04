class Board:

    NUMBER_ROWS = 6
    NUMBER_COLS = 7

    YELLOW = 1
    RED = 2
    BLANK = 0

    def __init__(self):
        self.stringifiedBoard = "0000000 0000000 0000000 0000000 0000000 0000000"
        self.currentBoard = [[0 for i in range(self.NUMBER_COLS)] for j in range(self.NUMBER_ROWS)]
        self.previousBoards = []
        self.previousMoves = []
        self.actionSpace = [i for i in range(self.NUMBER_COLS)]
        self.legalActions = [i for i in range(self.NUMBER_COLS)]
        self.movesMade = 0
    
    def stringifyBoard(self, arrayBoard):
        stringifiedBoard = ""

        for row_no in range(self.NUMBER_ROWS):
            for col_no in range(self.NUMBER_COLS):
                stringifiedBoard += str(arrayBoard[row_no][col_no])
            stringifiedBoard += " "
        
        return stringifiedBoard
    
    def stringToListBoard(self, stringifiedBoard):
        listifiedBoard = []
        rowList = stringifiedBoard.split(' ')

        for row in rowList:
            currentRow = []
            for char in row:
                currentRow.append(char)
            listifiedBoard.append(currentRow)
        
        return listifiedBoard


    def addPiece(self,column,color):
        for row_no in range(self.NUMBER_ROWS):
            if self.currentBoard[row_no][column] == self.BLANK:
                previousStringifiedBoard = self.stringifyBoard(self.currentBoard)
                previousBoards.append(previousStringifiedBoard)
                currentBoard[row_no][column] = color
                return True
        return False

    def checkLeftDiagonal(self):
        for i in range(len(self.NUMBER_ROWS)-1, 3, -1):
            for j in range(len(self.NUMBER_COLS)-1, 3, -1):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j-1]
                successorTwo = self.currentBoard[i+2][j-2]
                successorThree = self.currentBoard[i+3][j-3]
                    
                if origin != 0 and origin == successorOne and origin == successorTwo and origin == successorThree:
                    return True
        return False    

    def checkRightDiagonal(self):
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j+1]
                successorTwo = self.currentBoard[i+2][j+2]
                successorThree = self.currentBoard[i+3][j+3]

                if origin != 0 origin == successorOne and origin == successorTwo and origin == successorThree:
                    return True
        return False    

    def checkHorizontal(self):
        for i in range(self.NUMBER_ROWS):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i][j+1]
                successorTwo = self.currentBoard[i][j+2]
                successorThree = self.currentBoard[i][j+3]

                if origin != 0 origin == successorOne and origin == successorTwo and origin == successorThree:
                    return True
        
        return False
    
    def checkVertical(self):
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j]
                successorTwo = self.currentBoard[i+2][j]
                successorThree = self.currentBoard[i+3][j]

                if origin != 0 origin == successorOne and origin == successorTwo and origin == successorThree:
                    return True
        return False

    def checkWinner(self):
        if self.checkHorizontal or self.checkVertical or self.checkLeftDiagonal or self.checkRightDiagonal:
            return True
        return False

    def evaluateWindow(window):
        origin = window[0]
        for element in window:

    
    def evaluateReward(board: Board) -> int:
        if board.checkWinner():
            return 100
        



    

    
    

    

    



        

