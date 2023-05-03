# pylint: disable=C
import unittest
import blocker_functions

class TestBlockerFunctions(unittest.TestCase):
    def setUp(self):
        self.board = [[0 for i in range(10)] for j in range(10)]

    def test_addPlacementBlocker(self):
        positionTupelList = [(3, 3)]
        blocker_functions.addPlacementBlocker(self.board, positionTupelList)
        expected_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 6, 6, 6, 0, 0, 0, 0, 0],
            [0, 0, 6, 0, 6, 0, 0, 0, 0, 0],
            [0, 0, 6, 6, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.board, expected_board)

    def tearDown(self):
        del self.board

    # def test_addPlacementBlocker_out_of_bounds(self):
    #     positionTupelList = [(0, 0), (9, 9)]
    #     addPlacementBlocker(self.board, positionTupelList)
    #     expected_board = [
    #         [6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [6, 1, 6, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 6, 6, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 6, 0, 6, 0, 0, 0, 0],
    #         [0, 0, 0, 6, 1, 6, 0, 0, 0, 0],
    #         [0, 0, 0, 6, 0, 6, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 6, 6, 0],
    #         [0, 0, 0, 0, 0, 0, 6, 1, 6, 0],
    #         [0, 0, 0, 0, 0, 0, 6, 6, 0, 0],
    #         [0, 0,


if __name__ == "__main__":
    unittest.main()
