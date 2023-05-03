# pylint: disable=C
import unittest
from unittest.mock import patch, MagicMock
import select_operations

class TestStartingPlayerSelection(unittest.TestCase):
    @patch("builtins.input", return_value="j")
    def test_load_game_with_available_storage(self):
        result = select_operations.load_request.return_value = True
        self.assertTrue(result)

    @patch("builtins.input", return_value="n")
    def test_load_game_without_available_storage(self):
        result = select_operations.load_request.return_value = False
        self.assertFalse(result)

    @patch("builtins.input", return_value="invalid_input")
    def test_invalid_input(self):
        select_operations.load_request = MagicMock()
        result = select_operations.load_request
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
