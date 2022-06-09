import sys

from GUI.GameRoot import ConnectFour
from Algorithms.BoardJSON import BoardJSON


def main():
    game = ConnectFour()
    
    while not game.exitMainLoop:
        game.update_idletasks()
        game.update() 


if __name__ == '__main__':
    main()