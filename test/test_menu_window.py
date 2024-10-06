import unittest
from unittest.mock import patch, MagicMock
import pygame
from menu_window import StartMenu, show_menu, Settings  # Импортируйте класс и функцию из вашего файла
import input_box

class TestStartMenu(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.menu = StartMenu()

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertIsInstance(self.menu.get_bord_size_input, input_box.InputBox)

    def test_get_bord_size(self):
        self.menu.get_bord_size_input.text = '5'
        self.assertEqual(self.menu.get_bord_size(), '5')

    def test_draw_settings(self):
        # Call draw_settings method
        try:
            self.menu.draw_settings()
        except Exception as e:
            self.fail(f"draw_settings raised an exception: {e}")

    def test_draw_buttons(self):
        # Call draw_buttons method
        try:
            self.menu.draw_buttons()
        except Exception as e:
            self.fail(f"draw_buttons raised an exception: {e}")

    @patch('pygame.event.get', side_effect=[[], [MagicMock(type=pygame.event.Event), MagicMock(type=pygame.event.Event)]])
    def test_show_menu_exit(self, mock_event_get):
        exit_event = MagicMock(type=pygame.event.Event)
        exit_event.type = pygame.QUIT
        mock_event_get.side_effect = [[exit_event]]

        with self.assertRaises(SystemExit):  # Проверяем, что происходит выход из программы
            show_menu()

    @patch('pygame.event.get')
    def test_show_menu_click_single(self, mock_event_get):
        mouse_event = MagicMock(type=pygame.event.Event)
        mouse_event.type = pygame.MOUSEBUTTONDOWN
        mouse_event.pos = (110, 30)  # координаты кнопки "Против бота"

        mock_event_get.return_value = [mouse_event]

        result = show_menu()
        self.assertEqual(result.state, "single")
        self.assertEqual(result.bord_size, 9)

    @patch('pygame.event.get')
    def test_show_menu_click_multi(self, mock_event_get):
        mouse_event = MagicMock(type=pygame.event.Event)
        mouse_event.type = pygame.MOUSEBUTTONDOWN
        mouse_event.pos = (110, 80)  # координаты кнопки "Вдвоём"

        mock_event_get.return_value = [mouse_event]

        result = show_menu()
        self.assertEqual(result.state, "multi")
        self.assertEqual(result.bord_size, 9)

    @patch('pygame.event.get')
    def test_show_menu_click_exit(self, mock_event_get):
        mouse_event = MagicMock(type=pygame.event.Event)
        mouse_event.type = pygame.MOUSEBUTTONDOWN
        mouse_event.pos = (110, 130)  # координаты кнопки "Выйти"

        mock_event_get.return_value = [mouse_event]

        result = show_menu()
        self.assertEqual(result.state, "exit")
        self.assertEqual(result.bord_size, 9)


if __name__ == '__main__':
    unittest.main()