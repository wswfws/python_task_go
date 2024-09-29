import unittest
import score_counter
from GoGame import GoGameLogic, GoGameGUI
from config import BoardConfig
from test_boards import import_board


class TestGoGame(unittest.TestCase):

    def setUp(self):
        self.board_config = BoardConfig()
        # self.game_logic = GoGameLogic(9, self.board_config)
        # self.gui = GoGameGUI(self.game_logic, None)

    def test_place_stone(self):
        """Проверка размещения камня на доске"""
        self.game_logic = GoGameLogic(9, self.board_config)
        self.game_logic.place_stone(4, 4)
        self.assertEqual(self.game_logic.board[4][4], 'B')
        self.assertEqual(self.game_logic.current_player, 'W')

    def test_pass_move(self):
        """Проверка "паса" """
        self.game_logic = GoGameLogic(9, self.board_config)
        self.game_logic.pass_move()
        self.assertEqual(self.game_logic.black_score, 1)
        self.assertEqual(self.game_logic.white_score, 0)
        self.game_logic.end_game()
        self.assertEqual(self.game_logic.current_player, 'W')

    def test_end_game(self):
        """Проверка завершения игры"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_1"))
        self.game_logic.end_game()
        self.assertTrue(self.game_logic.game_over)

    def test_score_count_lite_filled_board(self):
        """Проверка счёта на доске без захватов чужих камней"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_1"))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 3)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 4)

    def test_score_count_filled_board_more_stones(self):
        """Проверка счёта на доске без захватов чужих камней, больше камней"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_2"))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 17)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 18)

    def test_score_count_placed_stones(self):
        """Проверка счёта после размещения камней"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_empty"))
        self.game_logic.place_stone(1, 1)
        self.game_logic.place_stone(0, 3)
        self.game_logic.place_stone(0, 1)
        self.game_logic.place_stone(0, 6)
        self.game_logic.place_stone(0, 2)
        self.game_logic.place_stone(1, 4)
        self.game_logic.place_stone(1, 0)
        self.game_logic.place_stone(1, 5)
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 5)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 6)

    def test_score_count_filled_board_holes(self):
        """Проверка счёта на доске с окружением, но без захвата (из-за дыр)"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_empty_holes"))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 12)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 2)

    # Какие-то траблы с подсчетом, хотя в GUI всё работает...
    def test_score_count_filled_captured_easy(self):
        """Проверка счёта на доске с захватом чужих камней"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_captured_easy"))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 3)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 4)

    def test_score_count_filled_board_captured(self):
        """Проверка счёта на доске с захватом чужих камней"""
        self.game_logic = GoGameLogic(9, self.board_config, import_board("board9x9_captured"))
        self.game_logic.end_game()
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[0], 12)
        self.assertEqual(score_counter.count_chinese_score(self.game_logic.board)[1], 19)


if __name__ == '__main__':
    unittest.main()