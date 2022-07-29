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
        self.guiCanvasType = None
        self.boardFilled = False
        self.winner = None
    
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
                self.previousBoards.append(previousStringifiedBoard)
                self.currentBoard[row_no][column] = color
                self.previousMoves.append(column)
                self.movesMade += 1
                return True
        return False

    def checkLeftDiagonal(self):
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(3, self.NUMBER_COLS-1):
                
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j-1]
                successorTwo = self.currentBoard[i+2][j-2]
                successorThree = self.currentBoard[i+3][j-3]

                if origin != 0 and origin == successorOne and origin == successorTwo and origin == successorThree:
                    self.winner = origin
                    return True
        return False   

    def checkRightDiagonal(self):
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j+1]
                successorTwo = self.currentBoard[i+2][j+2]
                successorThree = self.currentBoard[i+3][j+3]

                if origin != 0 and origin == successorOne and origin == successorTwo and origin == successorThree:
                    self.winner = origin
                    return True
        return False    

    def checkHorizontal(self):
        for i in range(self.NUMBER_ROWS):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i][j+1]
                successorTwo = self.currentBoard[i][j+2]
                successorThree = self.currentBoard[i][j+3]

                if origin != 0 and origin == successorOne and origin == successorTwo and origin == successorThree:
                    self.winner = origin
                    return True
        return False
    
    def checkVertical(self):
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j]
                successorTwo = self.currentBoard[i+2][j]
                successorThree = self.currentBoard[i+3][j]

                if origin != 0 and origin == successorOne and origin == successorTwo and origin == successorThree:
                    self.winner = origin
                    return True
        return False

    def checkWinner(self):
        if self.checkHorizontal() == True or self.checkVertical() == True or self.checkLeftDiagonal() == True or self.checkRightDiagonal() == True:
            return True
        return False
    
    def boardIsFilled(self):
        for i in range(self.NUMBER_ROWS):
            for j in range(self.NUMBER_COLS):
                if self.currentBoard[i][j] == self.BLANK:
                    return False
        self.boardFilled = True
        return True
                

    def evaluateWindow(self, window, piece):
        origin = window[0]
        windowScore = 0

        opponentPiece = 2 if piece == 1 else 1

        if window.count(piece) == 4:
            windowScore += 100
        elif window.count(piece) == 3 and window.count(self.BLANK) == 1:
            windowScore += 5
        elif window.count(piece) == 2 and window.count(self.BLANK) == 2:
            windowScore += 1
        if window.count(opponentPiece) == 3 and window.count(0) == 1:
            window_score -= 5
        elif window.count(opponentPiece) == 4:
            window_score -= 10000
        
        return windowScore

    def getWinner(self):
        return self.winner
    
    def evaluateReward(self, board, piece):
        reward = 0

        #horizontal windows
        for i in range(self.NUMBER_ROWS):
            for j in range(self.NUMBER_COLS - 3):
                origin = board[i][j]
                successorOne = board[i][j+1]
                successorTwo = board[i][j+2]
                successorThree = board[i][j+3]

                window = [origin, successorOne, successorTwo, successorThree]
                reward += self.evaluateWindow(self, window, piece)

        #vertical windows
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j]
                successorTwo = self.currentBoard[i+2][j]
                successorThree = self.currentBoard[i+3][j]

                window = [origin, successorOne, successorTwo, successorThree]
                reward += self.evaluateWindow(self, window, piece)

        #left diagonal windows
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j+1]
                successorTwo = self.currentBoard[i+2][j+2]
                successorThree = self.currentBoard[i+3][j+3]

                window = [origin, successorOne, successorTwo, successorThree]
                reward += self.evaluateWindow(self, window, piece)
        #right diagonal windows
        for i in range(self.NUMBER_ROWS - 3):
            for j in range(self.NUMBER_COLS - 3):
                origin = self.currentBoard[i][j]
                successorOne = self.currentBoard[i+1][j+1]
                successorTwo = self.currentBoard[i+2][j+2]
                successorThree = self.currentBoard[i+3][j+3]

                window = [origin, successorOne, successorTwo, successorThree]
                reward += self.evaluateWindow(self, window, piece)
        
        return reward

    def setGUICanvasType(self, x):
        self.guiCanvasType = x
