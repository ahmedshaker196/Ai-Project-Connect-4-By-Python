import math
import random
from ai.evaluation import Evaluation
from rules.win_checker import WinChecker
from board.board import ROW_COUNT, COLUMN_COUNT, Board

AI_PIECE = 2
PLAYER_PIECE = 1

class MinimaxAI:

    def get_valid_locations(self, board_obj):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if board_obj.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def is_terminal_node(self, board_obj):
        board = board_obj.board
        return WinChecker.winning_move(board, PLAYER_PIECE) or WinChecker.winning_move(board, AI_PIECE) or len(self.get_valid_locations(board_obj)) == 0

    def score_position(self, board, piece):
        # minimal wrapper: users can expand this
        from ai.evaluation import Evaluation
        score = 0
        # center control (simple)
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3
        return score

    def minimax(self, board_obj, depth, alpha, beta, maximizingPlayer):
        board = board_obj.board
        valid_locations = self.get_valid_locations(board_obj)

        is_terminal = self.is_terminal_node(board_obj)

        if depth == 0 or is_terminal:
            if is_terminal:
                if WinChecker.winning_move(board, AI_PIECE):
                    return (None, 1e14)
                elif WinChecker.winning_move(board, PLAYER_PIECE):
                    return (None, -1e14)
                else:
                    return (None, 0)
            else:
                return (None, self.score_position(board, AI_PIECE))

        if maximizingPlayer:
            value = -math.inf
            best_col = random.choice(valid_locations)

            for col in valid_locations:
                row = board_obj.get_next_open_row(col)
                temp = Board()
                temp.board = board.copy()
                temp.drop_piece(row, col, AI_PIECE)

                new_score = self.minimax(temp, depth-1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    best_col = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return best_col, value

        else:
            value = math.inf
            best_col = random.choice(valid_locations)

            for col in valid_locations:
                row = board_obj.get_next_open_row(col)
                temp = Board()
                temp.board = board.copy()
                temp.drop_piece(row, col, PLAYER_PIECE)

                new_score = self.minimax(temp, depth-1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    best_col = col

                beta = min(beta, value)
                if alpha >= beta:
                    break

            return best_col, value
