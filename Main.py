import sys

from GUI.GameRoot import ConnectFour
from Algorithms.BoardJSON import BoardJSON


def main():
    game = ConnectFour()
    
    while not game.exitMainLoop:
        if game.canvasIsMainWindow:
            gameCanvas = game.MainWindow
            if gameCanvas.humanTurn:
                gameCanvas.generateHumanTurn()
            else:
                gameCanvas.generateAITurn()
        game.update_idletasks()
        game.update() 


if __name__ == '__main__':
    main()