# pylint: disable=C
import unittest
import python_game
from unittest.mock import MagicMock
from converter_functions import split_column_converter, split_row

class TestPythonGame(unittest.TestCase):
    def setUp(self):
        self.board = [[0] * 10] * 10
        self.data = {
            "leaked_board_1": [[0]*10 for _ in range(10)],
            "leaked_board_2": [[0]*10 for _ in range(10)],
            "hidden_board_1": [[0]*10 for _ in range(10)],
            "hidden_board_2": [[0]*10 for _ in range(10)],
        }

    def test_split_column_converter(self):
        self.assertEqual(split_column_converter("A1"), 0)
        self.assertEqual(split_column_converter("b2"), 1)
        self.assertEqual(split_column_converter("J3"), 9)
        self.assertEqual(split_column_converter("Z1"), 25)

    def test_split_row(self):
        self.assertEqual(split_row("A1"), 0)
        self.assertEqual(split_row("b2"), 1)
        self.assertEqual(split_row("J3"), 2)
        self.assertEqual(split_row("11"), 0)

    def test_initialize_board(self):
        python_game.initialize_board = MagicMock()
        python_game.initialize_board.return_value = [[0] * 10] * 10
        result = python_game.initialize_board(self.board)
        self.assertEqual(self.board, result)

    def test_board_loader_load_available_false(self):
        python_game.board_loader(self.data, False)

        # check if boards are initialized
        self.assertEqual(len(self.data["leaked_board_1"]), 10)
        self.assertEqual(len(self.data["leaked_board_1"]), 10)
        self.assertEqual(len(self.data["leaked_board_2"]), 10)
        self.assertEqual(len(self.data["leaked_board_2"]), 10)
        self.assertEqual(len(self.data["hidden_board_1"]), 10)
        self.assertEqual(len(self.data["hidden_board_1"]), 10)
        self.assertEqual(len(self.data["hidden_board_2"]), 10)
        self.assertEqual(len(self.data["hidden_board_2"]), 10)

    def test_board_loader_load_available_true(self):
        self.data["leaked_board_1"] = [[1]*10 for _ in range(10)]
        self.data["leaked_board_2"] = [[1]*10 for _ in range(10)]
        self.data["hidden_board_1"] = [[1]*10 for _ in range(10)]
        self.data["hidden_board_2"] = [[1]*10 for _ in range(10)]

        python_game.board_loader(self.data, True)

        # check if boards are loaded correctly
        self.assertEqual(self.data["leaked_board_1"], [[1]*10 for _ in range(10)])
        self.assertEqual(self.data["leaked_board_2"], [[1]*10 for _ in range(10)])
        self.assertEqual(self.data["hidden_board_1"], [[1]*10 for _ in range(10)])
        self.assertEqual(self.data["hidden_board_2"], [[1]*10 for _ in range(10)])

    def test_board_reset(self):
        data = {
            "leaked_board_1": [[0,0],[0,0]],
            "leaked_board_2": [[1,1],[1,1]],
            "hidden_board_1": [[2,2],[2,2]],
            "hidden_board_2": [[3,3],[3,3]],
            "reset_board": [[0,0],[0,0]]
        }
        python_game.board_reset(data)
        expected_board = [[0,0],[0,0]]
        self.assertEqual(data["leaked_board_1"], expected_board)
        self.assertEqual(data["leaked_board_2"], expected_board)
        self.assertEqual(data["hidden_board_1"], expected_board)
        self.assertEqual(data["hidden_board_2"], expected_board)
    
    def test_board_reset_with_different_default_board(self):
        data = {
            "leaked_board_1": [[0,0],[0,0]],
            "leaked_board_2": [[1,1],[1,1]],
            "hidden_board_1": [[2,2],[2,2]],
            "hidden_board_2": [[3,3],[3,3]],
            "reset_board": [[0,0],[0,0]]
        }
        python_game.board_reset(data)
        expected_board = [[0,0],[0,0]]
        self.assertEqual(data["leaked_board_1"], expected_board)
        self.assertEqual(data["leaked_board_2"], expected_board)
        self.assertEqual(data["hidden_board_1"], expected_board)
        self.assertEqual(data["hidden_board_2"], expected_board)

    # def test_printleakedBoard(self):
    #     python_game.printleakedBoard = MagicMock()
    #     expected_output = "  \\\\ A B C D E F G H I J\n01  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n02  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n03  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n04  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n05  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n06  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n07  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n08  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n09  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n10  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
    #     result = python_game.initialize_board(self.board)
    #     with StringIO() as buf, redirect_stdout(buf):
    #         python_game.printleakedBoard(self.board)
    #         self.assertEqual(result, expected_output)

    # def test_printhiddenBoard(self):
    #     python_game.printhiddenBoard = MagicMock()
    #     expected_output = "  \\\\ A B C D E F G H I J\n01  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n02  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n03  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n04  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n05  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n06  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n07  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n08  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n09  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n10  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
    #     with StringIO() as buf, redirect_stdout(buf):
    #         self.printhiddenBoard(self.board)
    #         self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
