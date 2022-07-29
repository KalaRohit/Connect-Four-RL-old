import json
import os

from Algorithms.Environment import Board

class Parser():
    def __init__(self, filename):
        self.filename = filename
    
    def parseFile(self):
        loadedBoard = None
        with open(f'Saved Boards/{self.filename}.JSON', 'r') as file:
            board_dict = json.load(file)
            loadedBoard = Board()
            loadedBoard.__dict__ = board_dict
        return loadedBoard

