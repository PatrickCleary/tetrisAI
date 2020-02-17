
import tetris
import strategies
import TetrisAI

if __name__ == '__main__':
    strategist = strategies.strategist(.9, 2, 1.2)
    player = TetrisAI.tetrisplayer(strategist)
    tetris.playTetris(player)