import json
import os



class BoardJSON:
    def __init__(self, board, filename):
        jsonDump = json.dumps(board.__dict__)
        f = open(f'Saved Boards/{filename}.JSON', 'w')
        f.write(jsonDump)
        f.close()


