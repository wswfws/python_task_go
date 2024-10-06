import unittest
from unittest.mock import patch, MagicMock
import pygame
from game_over_window import End, show_end  # Импортируйте класс и функцию из вашего файла


class TestEnd(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.end = End(5, 3)  # Примерные очки

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertEqual(self.end.black_score, 5)
        self.assertEqual(self.end.white_score, 3)
        self.assertIsInstance(self.end.screen, pygame.Surface)

    def test_draw(self):
        # Проверяем, что метод draw не вызывает исключений
        try:
            self.end.draw()
        except Exception as e:
            self.fail(f"draw raised an exception: {e}")

    def test_draw_buttons(self):
        # Проверяем, что метод draw_buttons не вызывает исключений
        try:
            self.end.draw_buttons()
        except Exception as e:
            self.fail(f"draw_buttons raised an exception: {e}")

    @patch('pygame.event.get', side_effect=[[], [MagicMock(type=pygame.event.Event)]])
    def test_show_end_exit(self, mock_event_get):
        exit_event = MagicMock(type=pygame.event.Event)
        exit_event.type = pygame.QUIT
        mock_event_get.side_effect = [[exit_event]]

        with self.assertRaises(SystemExit):  # Проверяем, что происходит выход из программы
            show_end(5, 3)


if __name__ == '__main__':
    unittest.main()
