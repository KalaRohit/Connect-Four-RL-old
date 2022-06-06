from tkinter import *
from tkinter import messagebox


class MainMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)
        self.pack()

    def create_menu(self):
        yellow_button = Button(self, text='Start a new game as yellow', width= 30,command=self.set_board_up_yellow).pack()
        red_button = Button(self, width= 30, command=self.set_board_up_red, text='Start a new game as red').pack()
        two_npc = Button(self, width= 30,command=self.set_board_up_ai, text='Spectate a game between AI').pack()
        two_player = Button(self, width= 30,text='Local Multiplayer Game', command=self.set_board_up_multiplayer).pack()
    
    def set_board_up_yellow(self):
        self.master.create_board(0)
    
    def set_board_up_red(self):
        self.master.create_board(1)

    def set_board_up_ai(self):
        self.master.create_board(2)
    
    def set_board_up_multiplayer(self):
        self.master.create_board(3)
