import configuration as cfg
import unittest


class TestBoardConfig(unittest.TestCase):

    def setUp(self):
        self.config = cfg.BoardConfig()

    def test_GRID_CELL_SIZE(self):
        grid_cell_size = self.config.GRID_CELL_SIZE()
        self.assertEqual(grid_cell_size, cfg.WINDOW_WIDTH // 9)

    def test_STONE_RADIUS(self):
        stone_radius = self.config.STONE_RADIUS()
        self.assertEqual(stone_radius, cfg.WINDOW_WIDTH // 27)
