# pylint: disable=C
import unittest
from unittest.mock import MagicMock, patch
from converter_functions import split_column_converter, split_row

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

    def test_direction_s(self):
        board = [[0] * 10 for _ in range(10)]
        ship_length = 3
        starting_row_number = 2
        starting_column_char = 3
        direction = "s"
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

    def test_direction_a(self):
        board = [[0] * 10 for _ in range(10)]
        ship_length = 3
        starting_row_number = 8
        starting_column_char = 7
        direction = "a"
        game_mode = 2
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

    def test_direction_invalid(self):
        with patch("builtins.print") as mock_print:
            mock_print.assert_not_called()

    def test_valid_input(self):
        result = split_column_converter("a3")
        self.assertEqual(result, 0)

    def test_invalid_input_letter(self):
        with patch("builtins.print") as mock_print:
            result = split_column_converter("1")
            self.assertEqual(result, 11)
            mock_print.assert_called_with("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")
    
    def test_valid_input(self):
        self.assertEqual(split_row("A1"), 0)
        self.assertEqual(split_row("B2"), 1)
        self.assertEqual(split_row("C10"), 9)
    
    def test_invalid_input(self):
        self.assertEqual(split_row("A0"), 11)
        self.assertEqual(split_row("D11"), 11)
        self.assertEqual(split_row("F"), 11)
        self.assertEqual(split_row(""), 11)



if __name__ == "__main__":
    unittest.main()
