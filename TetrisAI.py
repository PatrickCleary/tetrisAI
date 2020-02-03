import random
import tetris

class tetrisplayer(object):

    def __init__(self):
        self.policy = ""    
        self.nextMove = None

    def getmove(self, board, stone, stonex, stoney, gameover):
        return self.decidemove(board, stone, stonex, stoney, gameover)
    
    def decidemove(self, board, stone, stonex, stoney, gameover):
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
            return 'UP'

    def getMoves(self, board, stone, stonex, stoney):
        newboard = board.copy()
        for i in range(9):
            shapeNum = tetris.tetris_shapes.index(stone)
            stonex = i
            if(not tetris.check_collision(board, stone, (stonex, stoney))):
                return

            for j in range(tetris.tetris_rotations[shapeNum] -1):
                tetris.rotate_clockwise(stone)

        tetris.rotate_clockwise()
        print('')

    def printInfo(self):
        return 'ligma'