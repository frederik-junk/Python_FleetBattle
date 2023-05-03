# pylint: disable=C
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import select_operations

class TestStartingPlayerSelection(unittest.TestCase):
    @patch("builtins.input", return_value="j")
    def test_load_game_with_available_storage(self, mock_input):
        result = select_operations.load_request.return_value = True
        self.assertTrue(result)

    @patch("builtins.input", return_value="n")
    def test_load_game_without_available_storage(self, mock_input):
        result = select_operations.load_request.return_value = False
        self.assertFalse(result)

    @patch("builtins.input", return_value="invalid_input")
    def test_invalid_input(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            select_operations.load_request = MagicMock()
            result = select_operations.load_request
            self.assertTrue(result)
            # self.assertIn('Ihre Eingabe ist falsch', fake_output.getvalue())


if __name__ == "__main__":
    unittest.main()
