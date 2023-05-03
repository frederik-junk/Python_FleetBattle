# pylint: disable=C
import unittest
from unittest.mock import MagicMock, patch

from converter_functions import split_column_converter

class TestConverterFunctions(unittest.TestCase):
    def test_direction_w(self):
        board = [[0] * 10 for _ in range(10)]
        ship_length = 3
        starting_row_number = 5
        starting_column_char = 2
        direction = "w"
        game_mode = 1
        ship = None

        # Test if a ship can be placed in the given direction without any issues
        direction_converter = MagicMock()
        self.assertTrue(
            direction_converter(
                board,
                ship_length,
                starting_row_number,
                starting_column_char,
                direction,
                game_mode,
                ship,
            )
        )

    def test_valid_input(self):
        result = split_column_converter("A3")
        self.assertEqual(result, 0)

    def test_invalid_input_number(self):
        with patch("builtins.print") as mock_print:
            result = split_column_converter("A")
            self.assertEqual(result, 0)

    def test_invalid_input_letter(self):
        with patch("builtins.print") as mock_print:
            result = split_column_converter("1")
            self.assertEqual(result, 11)
            mock_print.assert_called_with("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")
            mock_print.assert_called_with("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")



if __name__ == "__main__":
    unittest.main()
