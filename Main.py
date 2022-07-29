import sys
import os, psutil

from GUI.GameRoot import ConnectFour
from Algorithms.BoardJSON import BoardJSON


def main():
    game = ConnectFour()
    while not game.exitMainLoop:
        game.update_idletasks()
        game.update()
        if game.canvasIsMainWindow:
            game.menu.showMenuOptions()
            gameCanvas = game.MainWindow
            if gameCanvas.humanTurn:
                gameCanvas.generateHumanTurn()
            else:
                gameCanvas.generateAITurn()
        else:
            game.menu.disableMenuOptions()
         


if __name__ == '__main__':
    main()