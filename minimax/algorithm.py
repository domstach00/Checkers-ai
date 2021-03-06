from copy import deepcopy
import pygame
from checkers.constants import EVAL_CALC_WHITE, EVAL_CALC_RED

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    moves = []
    obligated_moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
            if skip:
                obligated_moves.append(new_board)
    if obligated_moves:
        return obligated_moves
    else:
        return moves


def minimax_alpha_beta(position, depth, max_player, base_player, oponent, game, alpha, beta):
    if depth == 0 or position.winner() is not None:
        if base_player == WHITE:
            return position.evaluate(EVAL_CALC_WHITE), position
            # return position.evaluate(), position
        else:
            return position.evaluate(EVAL_CALC_RED), position
            # return -position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, base_player, game):
            evaluation = minimax_alpha_beta(move, depth - 1, False, base_player, oponent, game, alpha, beta)[0]
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if max_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, oponent, game):
            evaluation = minimax_alpha_beta(move, depth - 1, base_player, base_player, oponent, game, alpha, beta)[0]
            min_eval = max(min_eval, evaluation)
            beta = min(beta, evaluation)
            if min_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return min_eval, best_move


def minimax(position, depth, max_player, base_player, oponent, game):
    if depth == 0 or position.winner() is not None:
        if base_player == WHITE:
            return position.evaluate(EVAL_CALC_WHITE), position
        else:
            return position.evaluate(EVAL_CALC_RED), position


    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, base_player, game):
            evaluation = minimax(move, depth - 1, False, base_player, oponent, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, oponent, game):
            evaluation = minimax(move, depth - 1, base_player, base_player, oponent, game)[0]
            min_eval = max(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move



def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(1)

