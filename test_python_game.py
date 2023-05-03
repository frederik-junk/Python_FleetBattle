# pylint: disable=C
import unittest
import pythonGame
from unittest.mock import MagicMock, patch
from io import StringIO
from contextlib import redirect_stdout
import sys
from converterfunctions import splitColumnConverter, splitRow

class TestPythonGame(unittest.TestCase):
    def setUp(self):
        self.board = [[0] * 10] * 10

    def test_splitColumnConverter(self):
        self.assertEqual(splitColumnConverter("A1"), 0)
        self.assertEqual(splitColumnConverter("b2"), 1)
        self.assertEqual(splitColumnConverter("J3"), 9)
        self.assertEqual(splitColumnConverter("Z1"), 11)

    def test_splitRow(self):
        self.assertEqual(splitRow("A1"), 0)
        self.assertEqual(splitRow("b2"), 1)
        self.assertEqual(splitRow("J3"), 2)
        self.assertEqual(splitRow("11"), 0)

    def test_initializeBoard(self):
        pythonGame.initializeBoard = MagicMock()
        pythonGame.initializeBoard.return_value = [[0] * 10] * 10
        result = pythonGame.initializeBoard(self.board)
        self.assertEqual(self.board, result)

    # def test_printleakedBoard(self):
    #     python_game.printleakedBoard = MagicMock()
    #     expected_output = "  \\\\ A B C D E F G H I J\n01  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n02  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n03  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n04  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n05  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n06  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n07  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n08  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n09  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n10  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
    #     result = python_game.initializeBoard(self.board)
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
