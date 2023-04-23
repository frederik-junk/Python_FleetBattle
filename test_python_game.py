import unittest
from unittest.mock import patch
from io import StringIO
import python_game

class TestPythonGame(unittest.TestCase):

    def setUp(self):
        self.leakedBoard1 = []
        for i in range(10):
            row = []
            for j in range(10):
                row.append(0)
            self.leakedBoard1.append(row)

        self.leakedBoard2 = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(0)
            self.leakedBoard2.append(row)

    def test_place_ship(self):
        with patch('builtins.input', side_effect=['A1', 'down']):
            python_game.placeShip(self.leakedBoard1, 3, [1,1,1], 'TestShip', 1)
        self.assertEqual(self.leakedBoard1[0][0], 1)
        # self.assertEqual(self.leakedBoard[1][0], 1)
        # self.assertEqual(self.leakedBoard[2][0], 1)

    # def test_ship_direction(self):
    #     self.leakedBoard[0][0] = 1
    #     with patch('builtins.input', side_effect=['down']):
    #         self.assertTrue(python_game.shipDirection(self.leakedBoard, 3, 0, 0, [1,1,1]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_leaked_board(self, mock_stdout):
        self.leakedBoard1[0][0] = 1
        self.printleakedBoard(self.leakedBoard1)
        self.assertIn('A B C D E F G H I J', mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_print_hidden_board(self, mock_stdout):
    #     self.hiddenBoard[0][0] = 1
    #     self.printhiddenBoard(self.hiddenBoard)
    #     self.assertIn('A B C D E F G H I J', mock_stdout.getvalue())

    def tearDown(self):
        del self.leakedBoard1
        del self.hiddenBoard1

if __name__ == '__main__':
    unittest.main()
