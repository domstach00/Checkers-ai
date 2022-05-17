import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQARE_SIZE
    col = x // SQARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())

        if IS_AI and game.turn == WHITE:
            value, new_board = minimax(game.get_board(), AI_WHITE_DEPTH, WHITE, WHITE, RED, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(f'White: {game.board.white_left} Red: {game.board.red_left} Winner: {game.winner()}')
            break

        if IS_AI_VS_AI:
            if game.turn == RED:
                value, new_board = minimax(game.get_board(), AI_RED_DEPTH, RED, RED, WHITE, game)
                game.ai_move(new_board)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        game.update()

    pygame.quit()


main()
