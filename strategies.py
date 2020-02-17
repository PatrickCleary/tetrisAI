


class strategist(object):
    def __init__(self, rowMultiplierWeight, holeWeight, heightWeight):
        self.rowMultiplierWeight = rowMultiplierWeight
        self.holeWeight = holeWeight
        self.heightWeight = heightWeight
        self.scores = []

    def gameover(self, score):
        self.scores.append(score)
        print(score)


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