
import tetris
import strategies
import TetrisAI
import random
import sys
from statistics import median, mean

if __name__ == '__main__':

    strategistArray = []
    stratsArray = []
    strategistScoresArray =[]
    numStrats = int(sys.argv[1])
    numTrials = int(sys.argv[2])

    for i in range(numStrats):
        strat = (random.random()*1, random.random()*2, random.random()*2)
        strat = (.95, 2, 1.2)
        stratsArray.append(strat)
        strategistArray.append(strategies.strategist(strat))

        scoresArray = []

        for j in range(numTrials):
            player = TetrisAI.tetrisplayer(strategistArray[i], 3)
            score = tetris.playTetris(player)
            scoresArray.append(score)

        strategistScoresArray.append(scoresArray)
    
    for i in range(numStrats):
        print('strat = ', stratsArray[i][0],'-', stratsArray[i][1],'-', stratsArray[i][2], 'median=', median(strategistScoresArray[i]), 'average = ', mean(strategistScoresArray[i]) )