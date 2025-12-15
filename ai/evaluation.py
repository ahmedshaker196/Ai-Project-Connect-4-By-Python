import random
from board.board import Board, ROW_COUNT, COLUMN_COUNT


EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4

class Evaluation:

    def get_valid_locations(self, board_obj):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if board_obj.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board_obj, piece):
        score = 0
        board_grid = board_obj.board

        # العمود الأوسط
        center_array = [int(i) for i in list(board_grid[:, COLUMN_COUNT // 2])]
        score += center_array.count(piece) * 3

        # الأفقي
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board_grid[r, :])]
            for c in range(COLUMN_COUNT - 3):  
                score += self.evaluate_window(row_array[c:c + WINDOW_LENGTH], piece)

        # الرأسي
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board_grid[:, c])]
            for r in range(ROW_COUNT - 3): 
                score += self.evaluate_window(col_array[r:r + WINDOW_LENGTH], piece)

        # القُطري الموجب \
        for r in range(ROW_COUNT - 3):  
            for c in range(COLUMN_COUNT - 3):  
                window = [board_grid[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        # القُطري السالب /
        for r in range(ROW_COUNT - 3): 
            for c in range(COLUMN_COUNT - 3):  
                window = [board_grid[r + WINDOW_LENGTH - 1 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def pick_best_move(self, board_obj, piece):
        valid_locations = self.get_valid_locations(board_obj)
        best_score = -10000
        best_col = random.choice(valid_locations)

        for col in valid_locations:
            row = board_obj.get_next_open_row(col)
            temp_board = Board()
            temp_board.board = board_obj.board.copy()
            temp_board.drop_piece(row, col, piece)

            score = self.score_position(temp_board, piece)

            if score > best_score:
                best_score = score
                best_col = col

        return best_col
