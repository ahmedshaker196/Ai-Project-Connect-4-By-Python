from board.board import Board
from ai.minimax import MinimaxAI
from rules.win_checker import WinChecker
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = MinimaxAI()
        self.turn = random.randint(0,1)  # 0 = player, 1 = AI

    def switch_turn(self):
        self.turn = (self.turn + 1) % 2
