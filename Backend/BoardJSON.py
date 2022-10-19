import json
import os



class BoardJSON:
    def __init__(self, board, filename):
        jsonBoardDict = json.dumps(board.__dict__)
        f = open(f'Saved Boards/{filename}.JSON', 'w')
        f.write(jsonBoardDict)
        f.close()


