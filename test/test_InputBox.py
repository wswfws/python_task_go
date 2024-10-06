import unittest
from unittest.mock import MagicMock
import pygame
import configuration as cfg
from input_box import InputBox


class TestInputBox(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.input_box = InputBox(100, 100, 140, 32)

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertEqual(self.input_box.rect.x, 100)
        self.assertEqual(self.input_box.rect.y, 100)
        self.assertEqual(self.input_box.rect.w, 140)
        self.assertEqual(self.input_box.rect.h, 32)
        self.assertEqual(self.input_box.text, '')
        self.assertFalse(self.input_box.active)

    def test_handle_event_mouse_click(self):
        # Simulate mouse click inside the input box
        event = MagicMock()
        event.type = pygame.MOUSEBUTTONDOWN
        event.pos = (110, 110)  # Inside the box

        self.input_box.handle_event(event)
        self.assertTrue(self.input_box.active)

        # Simulate mouse click outside the input box
        event.pos = (300, 300)  # Outside the box
        self.input_box.handle_event(event)
        self.assertFalse(self.input_box.active)

    def test_handle_event_keydown(self):
        # Activate the input box
        self.input_box.active = True

        # Simulate typing text
        event = MagicMock()
        event.type = pygame.KEYDOWN
        event.unicode = 'a'
        event.key = pygame.K_a

        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, 'a')

        # Simulate backspace
        event.key = pygame.K_BACKSPACE
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, '')

        # Simulate pressing Enter
        event.key = pygame.K_RETURN
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, '')

    def test_update_resizes_box(self):
        # Set text to something longer
        self.input_box.text = 'long text'
        self.input_box.txt_surface = self.input_box.FONT.render(self.input_box.text, True, cfg.BUTTON_COLOR)

        # Call update method
        self.input_box.update()

        # Check if the width has increased
        self.assertGreater(self.input_box.rect.w, 140)

    def test_draw(self):
        # Set up for drawing
        self.input_box.text = 'test'
        self.input_box.txt_surface = self.input_box.FONT.render(self.input_box.text, True, cfg.BUTTON_COLOR)

        try:
            self.input_box.draw(self.screen)
        except Exception as e:
            self.fail(f"draw method raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
