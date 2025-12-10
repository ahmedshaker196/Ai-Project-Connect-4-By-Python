import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

class Board:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for row in range(ROW_COUNT):
            if self.board[row][col] == 0:
                return row

    def print_board(self):
        import numpy as _np
        print(_np.flip(self.board, 0))
