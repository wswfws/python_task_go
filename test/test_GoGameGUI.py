import unittest
import configuration as cfg

from unittest.mock import MagicMock, patch, call
from go_game_gui import GoGameGUI


class TestGoGameGUI(unittest.TestCase):
    def setUp(self):
        # Мок объекты для game_logic и surface
        self.mock_game_gui = MagicMock()
        self.mock_surface = MagicMock()

        # Параметры для game_logic и bordConfig
        self.mock_game_gui.black_score = 10
        self.mock_game_gui.white_score = 15
        self.mock_game_gui.board = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'B', '.', '.', '.', '.', '.', 'W', '.'],
            ['.', '.', '.', '.', 'B', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'W', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]

        # Мок для bordConfig
        self.mock_bordConfig = MagicMock()
        self.mock_bordConfig.GRID_CELL_SIZE.return_value = 40
        self.mock_bordConfig.STONE_RADIUS.return_value = 3
        self.mock_bordConfig.BOARD_SIZE = 9
        self.mock_game_gui.bordConfig = self.mock_bordConfig

        # Экземпляр GUI с мок-объектами
        self.gui = GoGameGUI(self.mock_game_gui, self.mock_surface)

    @patch('pygame.draw.line')
    @patch('pygame.draw.circle')
    @patch('pygame.font.Font')
    @patch('pygame.draw.rect')
    def test_draw(self, mock_draw_rect, mock_font_class, mock_draw_circle, mock_draw_line):
        """Проверка draw - вызывает ли все функции GUI"""

        # Мок для текста (scores и кнопки)
        mock_font = mock_font_class.return_value
        mock_font.render.return_value = MagicMock()

        # Вызываем основную функцию отрисовки
        self.gui.draw()

        # Проверка вызовов для отрисовки линий
        self.assertEqual(mock_draw_line.call_count, 18)

        # Проверка вызовов для отрисовки камней
        self.assertEqual(mock_draw_circle.call_count, 4)  # Мы знаем, что на доске 4 камня

        # Проверка вызовов для отрисовки текстов (очков игроков)
        mock_font.render.assert_any_call('Черные: 10', True, cfg.TEXT_COLOR)
        mock_font.render.assert_any_call('Белые: 15', True, cfg.TEXT_COLOR)

        # Проверка вызовов для отрисовки кнопки
        self.assertEqual(mock_draw_rect.call_count, 2)

        # Убедимся, что `blit` вызван для текстов очков и кнопки
        self.assertGreaterEqual(self.mock_surface.blit.call_count, 4)  # Два для очков, один для кнопки


    @patch('pygame.draw.line')
    def test_draw_lines(self, mock_draw_line):
        """Проверка draw_lines - верное рисование линий поля и вызова pygame.draw.line"""
        half_grid = 20
        window_end = 430    # Предполагаем, что WINDOW_WIDTH = 450

        self.gui.draw_lines(half_grid, window_end)

        # Ожидаем, что линии нарисованы 9 раз по вертикали и горизонтали
        self.assertEqual(mock_draw_line.call_count, 2 * 9)

    @patch('pygame.draw.circle')
    def test_draw_stones(self, mock_draw_circle):
        """Проверка draw_stones - верное рисование камней и вызов pygame.draw.circle"""
        half_grid = 20

        self.gui.draw_stones(half_grid)

        # Ожидаем 4 вызова для камней B и W (отрисовал 4 камня, которые есть на доске)
        self.assertEqual(mock_draw_circle.call_count, 4)

        # Проверяем правильность аргументов для вызова рисования черного камня
        # (x, y) = (half_grid + x * GRID_SIZE, half_grid + y * GRID_SIZE)
        # На позиции (1, 1) (то же самое, что (60, 60)) в таблице стоит черный камень с STONE_RADIUS = 3
        mock_draw_circle.assert_any_call(
            self.mock_surface, cfg.BLACK_STONE_COLOR,
            (60, 60), 3     # позиции камня B на (1,1)
        )

        # B на (2, 4)
        mock_draw_circle.assert_any_call(
            self.mock_surface, cfg.BLACK_STONE_COLOR,
            (180, 100), 3
        )

        # Аналогично прошлому для камня W на позиции (1,7)
        mock_draw_circle.assert_any_call(
            self.mock_surface, cfg.WHITE_STONE_COLOR,
            (300, 60), 3
        )

        # W на (2, 4)
        mock_draw_circle.assert_any_call(
            self.mock_surface, cfg.WHITE_STONE_COLOR,
            (180, 180), 3
        )

    @patch('pygame.font.Font')
    def test_draw_scores(self, mock_font_class):
        """Проверка вывода очков игроков на экран"""
        mock_font = mock_font_class.return_value
        mock_font.render.return_value = MagicMock()     # Мок для текста

        half_grid = 20
        self.gui.draw_scores(half_grid)

        # Вызван ли pендер текста для очков черных и белых
        mock_font.render.assert_any_call('Черные: 10', True, cfg.TEXT_COLOR)
        mock_font.render.assert_any_call('Белые: 15', True, cfg.TEXT_COLOR)

        # Вызван ли blit (рисовка на поверхности) для обоих текстов
        self.assertEqual(self.mock_surface.blit.call_count, 2)

    @patch('pygame.draw.rect')
    @patch('pygame.font.Font')
    def test_draw_buttons(self, mock_font_class, mock_draw_rect):
        """Проверка правильности отрисовки кнопки ПАС и ?"""
        mock_font = mock_font_class.return_value
        mock_font.render.return_value = MagicMock()  # Мок для текста

        half_grid = 20
        self.gui.draw_buttons(half_grid)

        # Вызван ли метод отрисовки прямоугольников (кнопок)
        self.assertEqual(mock_draw_rect.call_count, 2)

        expected_calls = [
            call("Пас", True, cfg.TEXT_COLOR),
            call("?", True, cfg.TEXT_COLOR)
        ]
        # Отрендерен ли текст для кнопки
        mock_font.render.has_calls(expected_calls, any_order=True)
        # Вызван ли blit для текста на кнопке
        self.assertEqual(self.mock_surface.blit.call_count, 2)


    @patch('pygame.draw.rect')
    @patch('pygame.font.Font')
    def test_draw_help(self, mock_font_class, mock_draw_rect):
        """Проверка правильности отрисовки кнопки правил"""
        mock_font = mock_font_class.return_value
        mock_font.render.return_value = MagicMock()  # Мок для текста

        self.gui.draw_help()

        # Вызван ли метод отрисовки прямоугольников (кнопок)
        self.assertEqual(mock_draw_rect.call_count, 2)

        expected_calls = [
            call("Правила игры", True, cfg.LINK_COLOR),
            call("P. S.: Для завершения игры два игрока должны спасовать", True, cfg.TEXT_COLOR)
        ]
        # Отрендерен ли текст для кнопки
        mock_font.render.has_calls(expected_calls, any_order=True)
        # Вызван ли blit для текста на кнопке
        self.assertEqual(self.mock_surface.blit.call_count, 2)



if __name__ == '__main__':
    unittest.main()
