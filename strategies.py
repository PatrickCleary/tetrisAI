


class strategist(object):
    def __init__(self, weights):
        self.rowMultiplierWeight = weights[0]
        self.holeWeight = weights[1]
        self.heightWeight = weights[2]
        self.scores = []

    def strategy1(self, board):
        summation = 1
        rowMultiplier = 1
        for i, row in enumerate(board[:-1]):
            rowMultiplier*=self.rowMultiplierWeight
            for j, value in enumerate(row):
                if value >0 and board[i+1][j] == 0:
                    summation +=self.holeWeight*rowMultiplier
                if value > 0:
                    summation += self.heightWeight*rowMultiplier
        return 1/summation