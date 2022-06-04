import sys

from GUI.GameRoot import ConnectFour


def main():
    game = ConnectFour()

    
    while True:
        game.update_idletasks()
        game.update()

        if game.exitMainLoop:
            break  


if __name__ == '__main__':
    main()