import copy
import random

from score_counter import count_chinese_score


def get_possible_moves(bord):
    size = len(bord)
    possible_moves = []

    for i in range(size):
        for j in range(size):
            if bord[i][j] == ".":
                possible_moves.append((i, j))
    return possible_moves


def get_random_move(bord, player):
    moves = get_possible_moves(bord)
    return random.choice(moves)


def get_deep_move(bord, player, deep=4):
    moves = get_possible_moves(bord)
    best_move = (0, get_random_move(bord, player))

    for move in moves:
        if deep == 1:
            score = count_chinese_score(bord)[0 if player == "B" else 1]
        else:
            new_board = copy.deepcopy(bord)
            new_board[move[0]][move[1]] = player
            next_player = 'W' if player == 'B' else 'B'
            next_move = get_deep_move(new_board, next_player, deep - 1)
            new_board[next_move[0]][next_move[1]] = next_player
            score = count_chinese_score(new_board)[0 if next_player == "B" else 1]
        if best_move[0] < score:
            best_move = (score, move)

    return best_move[1]
