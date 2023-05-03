# pylint: disable=C
import unittest
import blocker_functions

class TestBlockerFunctions(unittest.TestCase):
    def setUp(self):
        self.board = [[0 for i in range(10)] for j in range(10)]

    def test_add_placement_blocker(self):
        position_tupel_list = [(3, 3)]
        blocker_functions.add_placement_blocker(self.board, position_tupel_list)
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.board, expected_board)

    def test_add_placement_blocker_out_of_bounds(self):
        position_tupel_list = [(7, 7)]
        blocker_functions.add_placement_blocker(self.board, position_tupel_list)
        expected_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 6, 0],
            [0, 0, 0, 0, 0, 0, 6, 0, 6, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 6, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.board,expected_board)

    def tearDown(self):
        del self.board

    


if __name__ == "__main__":
    unittest.main()
