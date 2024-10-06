import random
import copy

from go_game_logic import GoGameLogic
from configuration import BoardConfig
from score_counter import count_chinese_score


def get_possible_moves(bord):
    size = len(bord)
    possible_moves = []

    for i in range(size):
        for j in range(size):
            if bord[i][j] == ".":
                possible_moves.append((i, j))
    return possible_moves


def get_random_move(board):
    moves = get_possible_moves(board)
    return random.choice(moves)


def heuristic_move(board, move, player):
    # Определяем, как хорошо этот ход выглядит на первый взгляд
    # Например, можно учитывать захват камней, расширение территории и прочее.

    new_board = GoGameLogic(len(board), BoardConfig(), copy.deepcopy(board), fake=True)
    new_board.place_stone(*move)

    # Простая эвристика: считаем разницу в оценке после хода
    score_before = count_chinese_score(board)[0 if player == "B" else 1]
    score_after = count_chinese_score(new_board.board)[0 if player == "B" else 1]

    # Оцениваем разницу в очках после хода
    score_delta = score_after - score_before

    # Дополнительно можно учитывать стратегические факторы, как занятые территории
    return score_delta


def get_deep_move(board, player, deep=2, alpha=-float('inf'), beta=float('inf')):
    moves = get_possible_moves(board)
    if not moves:
        return None

    # Сортируем ходы для более раннего отсечения
    moves = sorted(moves, key=lambda move: heuristic_move(board, move, player), reverse=True)
    best_move = (alpha, get_random_move(board))  # Инициализация лучшего хода

    for move in moves:
        if deep == 1:
            # Оцениваем позицию на текущем уровне
            score = count_chinese_score(board)[0 if player == "B" else 1]
        else:
            # Создаем новый вариант доски без глубокого копирования
            new_board = GoGameLogic(len(board), BoardConfig(), copy.deepcopy(board), fake=True)
            new_board.current_player = player
            new_board.place_stone(*move)
            next_player = 'W' if player == 'B' else 'B'

            # Рекурсивный вызов с уменьшенной глубиной
            next_move_score = get_deep_move(new_board.board, next_player, deep - 1, -beta, -alpha)
            if next_move_score is None:
                continue
            score = -next_move_score[0]  # Инвертируем оценку, так как ходы чередуются

        # Обновляем лучший ход, если текущий ход лучше
        if score > best_move[0]:
            best_move = (score, move)

        # Альфа-бета отсечение
        alpha = max(alpha, score)
        if alpha >= beta + 3:
            break  # Прерываем дальнейшую оценку, если нашли достаточно хороший ход

    # print(*board, sep = "\n")
    # print(best_move)
    # print("+"*50)
    return best_move[1]
