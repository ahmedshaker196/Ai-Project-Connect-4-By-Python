from core.game import Game
from gui.gui import GUI
import pygame, sys, math
from board.board import ROW_COUNT, COLUMN_COUNT
from rules.win_checker import WinChecker

pygame.init()

game = Game()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
gui = GUI(screen, SQUARESIZE)

gui.draw_board(game.board.board)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)

import time
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0,0,0), (0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if game.turn == 0:
                pygame.draw.circle(screen, (255,0,0), (posx, int(SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, (0,0,0), (0,0,width,SQUARESIZE))
            if game.turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if game.board.is_valid_location(col):
                    row = game.board.get_next_open_row(col)
                    game.board.drop_piece(row, col, 1)
                    if WinChecker.winning_move(game.board.board, 1):
                        label = myfont.render('Player 1 wins!!', 1, (255,0,0))
                        screen.blit(label, (40,10))
                        game_over = True
                    game.switch_turn()
                    gui.draw_board(game.board.board)

    # AI turn (simple call)
    if game.turn == 1 and not game_over:
        col, score = game.ai.minimax(game.board, 4, -math.inf, math.inf, True)
        if game.board.is_valid_location(col):
            row = game.board.get_next_open_row(col)
            game.board.drop_piece(row, col, 2)
            if WinChecker.winning_move(game.board.board, 2):
                label = myfont.render('AI wins!!', 1, (255,255,0))
                screen.blit(label, (40,10))
                game_over = True
            game.switch_turn()
            gui.draw_board(game.board.board)

    if game_over:
        pygame.time.wait(3000)
        sys.exit()
