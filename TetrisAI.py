import random
import tetris

class tetrisplayer(object):

    def __init__(self):
        self.policy = ""    
        self.nextMove = None

    def getmove(self, board, stone, stonex, stoney, gameover):
        return self.decidemove(board, stone, stonex, stoney, gameover)
    
    def decidemove(self, board, stone, stonex, stoney, gameover):
        maxMove = self.getMoves(board, stone)
        numiters = maxMove[1]-4
        return (numiters, maxMove[2])

        score = maxMove[0]
        if gameover:
            return 'SPACE'
        if(score<.2):
            return 'UP'
        if(score<.4):
            return 'DOWN'
        if(score<.6):
            return 'RIGHT'
        if(score<.8):
            return 'LEFT'
        else:
            return 'UP'

    def scoreBoard(self, board):

        return random.random()

    def getMoves(self, board, stone):
        maxMove = (0, 0, 0)
        for value in stone[0]:
            if(value > 0):
                shapeNum = value
        for i in range(8):
            stonex = i
            stoney = 0

            for j in range(tetris.tetris_rotations[shapeNum-1] -1):
                tetris.rotate_clockwise(stone)

                if tetris.check_collision(board, stone,(stonex, stoney)):
                    newBoard = board.copy()
                    newBoard = tetris.join_matrixes(newBoard, stone, (stonex, stoney))
                    score = self.scoreBoard(newBoard)
                    print(score)
                    if(score > maxMove[0]):
                        maxMove = (score, i, j)
        return maxMove

    def printInfo(self):
        return 'ligma'