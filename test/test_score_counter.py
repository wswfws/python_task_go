import unittest
import score_counter
import test_boards as boards

from go_game_logic import GoGameLogic
from configuration import BoardConfig
from copy import deepcopy


class TestGoGame(unittest.TestCase):
    def setUp(self):
        self.board_config = BoardConfig()

    def test_score_count_lite_filled_board(self):
        """Проверка счёта на доске без захватов чужих камней"""
        self.game_logic = GoGameLogic(9, self.board_config, deepcopy(boards.board9x9_1))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 3)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 4)

    def test_score_count_filled_board_more_stones(self):
        """Проверка счёта на доске без захватов чужих камней, больше камней"""
        self.game_logic = GoGameLogic(9, self.board_config, deepcopy(boards.board9x9_2))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 17)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 18)

    def test_score_count_filled_board_holes(self):
        """Проверка счёта на доске с окружением, но без захвата (из-за дыр)"""
        self.game_logic = GoGameLogic(9, self.board_config, deepcopy(boards.board9x9_empty_holes))
        self.game_logic.current_player = 'W'
        self.game_logic.place_stone(0, 0)  # W on (0, 0)
        self.game_logic.place_stone(2, 0)  # B on (2, 0) - made B's territory
        self.game_logic.place_stone(6, 7)  # W on (6, 7) on B's territory
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 12)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 3)

    def test_two_stones_in_one_cell(self):
        """Проверка счёта при помещения двух разных камней в одну и ту же клетку"""
        self.game_logic = GoGameLogic(9, self.board_config)
        self.game_logic.place_stone(1, 1)  # B
        self.game_logic.place_stone(1, 1)  # W - not located, 2nd attempt
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 0)

    def test_score_count_filled_captured_easy(self):
        """Проверка счёта на доске с захватом чужих камней"""
        self.game_logic = GoGameLogic(9, self.board_config, deepcopy(boards.board9x9_captured_easy))
        self.game_logic.current_player = 'W'
        self.game_logic.place_stone(0, 0)
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 3)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 4)

    def test_score_count_filled_captured_hard(self):
        """Проверка счёта на доске с захватом чужих камней, больше захватов"""
        self.game_logic = GoGameLogic(9, self.board_config, deepcopy(boards.board9x9_captured_hard))
        self.game_logic.place_stone(4, 4)  # B in W-circle (disappear)
        self.game_logic.place_stone(0, 0)  # W in B-territory
        self.game_logic.place_stone(6, 0)  # B in W-circle (disappear)
        self.game_logic.place_stone(1, 8)  # W in B-circle (disappear)
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 22)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 13)

    def test_score_count_13x13(self):
        """Проверка счёта на 13x13 доске"""
        self.game_logic = GoGameLogic(13, self.board_config, deepcopy(boards.board13x13_captured))
        self.game_logic.place_stone(0, 5)  # B in W-territory
        self.game_logic.place_stone(6, 0)  # W in B-territory
        self.game_logic.place_stone(0, 6)  # B in W-circle (disappear * 2)
        self.game_logic.place_stone(12, 12)  # W in B-circle (disappear)
        self.game_logic.place_stone(11, 9)  # B in W-territory
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 9)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 13)

    def test_score_count_19x19(self):
        """Проверка счёта на 19x19 доске"""
        self.game_logic = GoGameLogic(19, self.board_config, deepcopy(boards.board19x19_captured))
        self.game_logic.place_stone(4, 9)  # B in W-circle (disappear)
        self.game_logic.place_stone(1, 0)  # W in B-territory
        self.game_logic.place_stone(11, 0)  # B in W-territory
        self.game_logic.place_stone(13, 17)  # W in B-circle (disappear)
        self.game_logic.place_stone(11, 1)  # B in W-circle (disappear * 2)
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 16)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 13)


if __name__ == '__main__':
    unittest.main()
