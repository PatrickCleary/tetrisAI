import random
import tetris
import time
import copy

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

    def __init__(self):
        self.policy = ""    
        self.nextMove = None

    def getmove(self, board, stone, stonex, stoney, gameover):
        time.sleep(1)
        return self.decidemove(board, stone, stonex, stoney, gameover)
    
    def decidemove(self, board, stone, stonex, stoney, gameover):
        maxMove = self.getMoves(board, stone)
        numiters = maxMove[1]-3
        if gameover:
            return (1000, 1000)
        return (numiters, maxMove[2])

        score = maxMove[0]
       

    def scoreBoard(self, board):
        rowvalues = [0]*len(board)
        for i, row in enumerate(board[:-1]):
            summation =0
            for value in row:
                if value != 0:
                    summation+=1
            rowvalues[i] = summation
        return max(rowvalues)

    def drop(self, board, stone, stonex, stoney):
        stoney+=1
        if check_collision(board, stone, (stonex, stoney)):
            return join_matrixes(board, stone, (stonex, stoney))
        else:
            return self.drop(board, stone, stonex, stoney)
        
    def printboard(self, board):
        for row in board:
            print(row)
        pass

    def getMoves(self, board, stone):
        maxMove = (0, 0, 0)
        for value in stone[0]:
            if(value > 0):
                shapeNum = value
        for i in range(10):
            stonex = i
            stoney = 0
            for j in range(tetris.tetris_rotations[shapeNum-1]):

                newBoard = copy.deepcopy(board)
                if(check_collision(newBoard,stone,(stonex,stoney))):
                    print('collide')
                    print(stonex, stoney)
                    continue
                newBoard = self.drop(newBoard, stone, stonex, stoney)
                score = self.scoreBoard(newBoard)
                if(score > maxMove[0]):
                    maxMove = (score, i, j)
                stone = tetris.rotate_clockwise(stone)
        return maxMove

    def printInfo(self):
        return 'ligma'