import random
import tetris
import time
import copy
import strategies

def check_collision(board, shape, offset):
	off_x, off_y = offset
	for cy, row in enumerate(shape):
		for cx, cell in enumerate(row):
			try:
				if cell and board[ cy + off_y ][ cx + off_x ]:
					return True
			except IndexError:
				return True
	return False

def join_matrixes(mat1, mat2, mat2_off):
	off_x, off_y = mat2_off
	for cy, row in enumerate(mat2):
		for cx, val in enumerate(row):
			mat1[cy+off_y-1	][cx+off_x] += val
	return mat1

class tetrisplayer(object):

    def __init__(self, strategist, numGames):
        self.strategist = strategist    
        self.numGames = numGames
        self.gamesPlayed = 0

    def getmove(self, board, stone, stonex, stoney, gameover):
        return self.decidemove(board, stone, stonex, stoney, gameover)
    
    def decidemove(self, board, stone, stonex, stoney, gameover):
        maxMove = self.getMoves(board, stone)
        if gameover:
            self.gamesPlayed +=1
            if self.gamesPlayed == self.numGames:
                return (-1000 , -1000)
            else:
                return (1000, 1000)
        return (maxMove[1], maxMove[2])


    def scoreBoard(self, board):
        return self.strategist.strategy1(board)

    def drop(self, board, stone, stonex, stoney):
        stoney+=1
        if check_collision(board, stone, (stonex, stoney)):
            return join_matrixes(board, stone, (stonex, stoney))
        else:
            return self.drop(board, stone, stonex, stoney)
            
    def gameover(self, score):
        self.strategist.gameover(score)    
    
    def printboard(self, board):
        for row in board:
            print(row)
        pass

    def getMoves(self, board, stone):
        maxMove = (0, 0, 0)
        score = 0
        for value in stone[0]:
            if(value > 0):
                shapeNum = value
        for i in range(10):
            stonex = i
            stoney = 0
            for j in range(tetris.tetris_rotations[shapeNum-1]):
                newBoard = copy.deepcopy(board)
                if i > 10 - len(stone[0]):
                    stone = tetris.rotate_clockwise(stone)
                    continue
                
                newBoard = self.drop(newBoard, stone, stonex, stoney)
                score = self.scoreBoard(newBoard)
                if(score > maxMove[0]):
                    maxMove = (score, i, j)
                stone = tetris.rotate_clockwise(stone)
        return maxMove

    def printInfo(self):
        return 'ligma'