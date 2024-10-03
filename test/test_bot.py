import unittest
import copy
import bot
import test_boards as boards

from go_game_logic import GoGameLogic
from configuration import BoardConfig


class TestGoGameFunctions(unittest.TestCase):
    def setUp(self):
        self.board_size = 9
        self.board_config = BoardConfig()

    def test_get_possible_moves_number(self):
        """Проверка получения всех возможных ходов, по количеству"""
        board = [['.'] * 9 for _ in range(self.board_size)]
        board[6][6] = 'W'
        moves = bot.get_possible_moves(board)
        self.assertEqual(len(moves), self.board_size * self.board_size - 1)

    def test_get_possible_moves_quality(self):
        """Проверка получения всех возможных ходов, по содержанию"""
        board = boards.board3x3
        move = bot.get_random_move(board)
        possible_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        self.assertIn(move, possible_moves)

    def test_get_random_move(self):
        """Проверка получения произвольного хода робота"""
        board = [['.'] * 9 for _ in range(self.board_size)]
        board[6][6] = 'W'
        moves = bot.get_possible_moves(board)
        move = bot.get_random_move(board)
        self.assertIn(move, moves)

    def test_heuristic_move(self):
        """Проверка работоспособности дельта-сравнения счёта"""
        board = boards.board9x9_captured_easy_neg
        expected_score_delta = 2    # Estimated difference between the score after the move

        score_before = bot.count_chinese_score(board)[0]    # For Blacks
        new_board = GoGameLogic(len(board), BoardConfig(), copy.deepcopy(board), fake=True)
        new_board.place_stone(8, 6)     # Putting a new black stone
        score_after = bot.count_chinese_score(new_board.board)[0]
        self.assertAlmostEqual(score_after - score_before, expected_score_delta)

    def test_get_deep_move_none(self):
        """Проверка выкидывания None, если возможных ходов для робота нет"""
        board = [['A'] * 9 for _ in range(9)]
        result = bot.get_deep_move(board, 'B')
        self.assertIsNone(result)

    def test_get_deep_move(self):
        """Проверка правильности возвращаемого возможного хода при сложном анализе"""
        board = boards.board9x9_captured_easy_neg
        result = bot.get_deep_move(board, 'B')
        self.assertIsNotNone(result)
        self.assertIn(result, bot.get_possible_moves(board))


if __name__ == '__main__':
    unittest.main()
