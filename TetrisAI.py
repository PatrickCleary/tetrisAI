import random

class tetrisplayer(object):

    def __init__(self, board):
        self.policy = ""    
        self.board = board    
        self.nextMove = None

    def getmove(self, board, stone, stonex, stoney, gameover):
        return self.decidemove(board, stone, stonex, stoney, gameover)
    
    def decidemove(self,board, stone, stonex, stoney, gameover):
        x = random.random()
        if gameover:
            return 'SPACE'
        if(x<.2):
            return 'UP'
        if(x<.4):
            return 'DOWN'
        if(x<.6):
            return 'RIGHT'
        if(x<.8):
            return 'LEFT'
        else:
            return 'RETURN'
    def printInfo(self):
        return 'ligma'