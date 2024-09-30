import unittest
import test_boards as boards

from GoGame import GoGameLogic
from config import BoardConfig
from copy import deepcopy


class TestGoGame(unittest.TestCase):
    def setUp(self):
        self.board_config = BoardConfig()
        self.board_size = 9

    def test_place_stone_1_player(self):
        """Проверка размещения камня на доске"""
        self.game_logic = GoGameLogic(self.board_size, self.board_config)
        self.game_logic.place_stone(4, 4)
        self.assertEqual(self.game_logic.board[4][4], 'B')
        self.assertEqual(self.game_logic.current_player, 'W')

    def test_place_stone_2_players(self):
        """Проверка размещения камней на доске"""
        self.game_logic = GoGameLogic(self.board_size, self.board_config)
        self.game_logic.place_stone(4, 4)
        self.game_logic.place_stone(3, 3)
        self.assertEqual(self.game_logic.board[4][4], 'B')
        self.assertEqual(self.game_logic.board[3][3], 'W')
        self.assertEqual(self.game_logic.current_player, 'B')

    def test_bounds(self):
        """Проверка размещения в границах"""
        self.game_logic = GoGameLogic(self.board_size, self.board_config)
        self.assertEqual(self.game_logic.place_stone(-1, -5), False)

    def test_pass_move(self):
        """Проверка "паса" """
        self.game_logic = GoGameLogic(self.board_size, self.board_config)
        self.game_logic.pass_move()
        self.assertEqual(self.game_logic.black_score, 1)
        self.assertEqual(self.game_logic.white_score, 0)
        self.game_logic.end_game()
        self.assertEqual(self.game_logic.current_player, 'W')

    def test_end_game(self):
        """Проверка завершения игры"""
        self.game_logic = GoGameLogic(self.board_size, self.board_config, deepcopy(boards.board9x9_1))
        self.game_logic.end_game()
        self.assertTrue(self.game_logic.game_over)

    def test_two_stones_in_one_cell(self):
        """Проверка попытки помещения двух разных камней в одну и ту же клетку"""
        self.game_logic = GoGameLogic(self.board_size, self.board_config)
        self.game_logic.place_stone(1, 1)   # B
        self.game_logic.place_stone(1, 1)   # W - not located, 2nd attempt
        self.game_logic.end_game()
        self.assertEqual(self.game_logic.board[1][1], 'B')
        self.assertEqual(self.game_logic.current_player, 'W')


if __name__ == '__main__':
    unittest.main()
