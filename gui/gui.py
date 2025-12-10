import pygame
from board.board import ROW_COUNT, COLUMN_COUNT

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

class GUI:
    def __init__(self, screen, square_size):
        self.screen = screen
        self.SQUARESIZE = square_size
        self.width = COLUMN_COUNT * square_size
        self.height = (ROW_COUNT + 1) * square_size
        self.RADIUS = int(square_size / 2 - 5)

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(self.height - (r*self.SQUARESIZE + self.SQUARESIZE/2))), self.RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(self.screen, YELLOW, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(self.height - (r*self.SQUARESIZE + self.SQUARESIZE/2))), self.RADIUS)
        pygame.display.update()
