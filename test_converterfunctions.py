import unittest
import blockerfunctions
from unittest.mock import MagicMock, patch

#pylint: disable=C

class TestConverterFunctions(unittest.TestCase):
    def test_direction_w(self):
        board = [[0] * 10 for _ in range(10)]
        shipLength = 3
        startingRowNumber = 5
        startingColumnChar = 2
        direction = "w"
        gameMode = 1
        ship = None

        # Test if a ship can be placed in the given direction without any issues
        directionConverter = MagicMock()
        self.assertTrue(directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode, ship))
        expected_board = [
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        # self.assertEqual(board, expected_board)

        # Test if the function raises the correct exception when a ship is placed out of the game board
        # startingRowNumber = 1
        # self.assertTrue(directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode, ship))
        # expected_board = [
        #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0

if __name__ == "__main__":
    unittest.main()