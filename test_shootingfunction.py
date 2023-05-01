import unittest
from unittest.mock import patch
import io
import sys
import random
import circularImportFixing
import pythonGame
import converterfunctions
import outputmanager
import shootingfunction

class TestShooting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {}
        cls.currentPlayer = 1
        cls.gameMode = 1
        cls.user1 = "Testspieler"

        
    # @patch('builtins.input', side_effect=['A1'])
    # def test_playermanager_1(self, mock_input):
    #     global user1
    #     result = shootingfunction.playermanager(self.data, user1.getName(), leakedBoard2, hiddenBoard1, playerShips)
    #     self.assertEqual(result, None)

    # @patch('builtins.input', side_effect=['A1'])
    # def test_shooting_1(self, mock_input):
    #     result = shootingfunction.shooting(self.data, self.gameMode, self.currentPlayer)
    #     self.assertEqual(result, None)

    def test_playermanager(self):
        data = []
        currentPlayerName = "test"
        leakedBoard = [[0 for i in range(10)] for j in range(10)]
        hiddenBoard = [[0 for i in range(10)] for j in range(10)]
        shipList = []
        currentPlayer = 1
        with io.StringIO("A1\n") as mock_input:
            sys.stdin = mock_input
            output = shootingfunction.playermanager(data, currentPlayerName, leakedBoard, hiddenBoard, shipList, currentPlayer)
            self.assertIsNone(output)

    def test_nextPlayer_player1(self):
        # Test for currentPlayer == 1
        gameMode = "1"
        currentPlayer = 1
        data = {"currentPlayer": 1}
        expected_output = f"__________________________________\n{outputmanager.user2.getName()} ist nun an der Reihe.\n__________________________________\n"
        with patch('builtins.input', return_value='a'):
            with patch('sys.stdout', new=io.StringIO()) as fake_output:
                shootingfunction.nextPlayer(gameMode, currentPlayer, data)
                self.assertEqual(data["currentPlayer"], 1)
                
    def test_nextPlayer_error(self):
        # Test for invalid currentPlayer value
        gameMode = "easy"
        currentPlayer = 3
        data = {"currentPlayer": 3}
        expected_output = "Irgendwas ist hier schief gelaufen!\nShit\n"
        with patch('builtins.input', return_value='a'):
            with patch('sys.stdout', new=io.StringIO()) as fake_output:
                shootingfunction.nextPlayer(gameMode, currentPlayer, data)
                self.assertEqual(fake_output.getvalue(), expected_output)

    @patch('random.randint')
    def test_random_direction(self, mock_randint):
        # Set up the mock random integer function to return a known value
        mock_randint.return_value = 2
        
        # Call the function and assert that it returns the expected value
        result = shootingfunction.randomDirection()
        self.assertEqual(result, 2)

        # Assert that the mock random integer function was called with the expected arguments
        mock_randint.assert_called_once_with(0, 3)

    def test_missed_shot(self):
        hiddenBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        leakedBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        cpuMemory = (1, 1)

        result = shootingfunction.checkHit(hiddenBoard, leakedBoard, cpuMemory)

        self.assertEqual(result, 0)
        self.assertEqual(hiddenBoard, [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ])

    def test_water_hit(self):
        hiddenBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        leakedBoard = [
            [0, 0, 0],
            [0, 6, 0],
            [0, 0, 0]
        ]
        cpuMemory = (1, 1)

        result = shootingfunction.checkHit(hiddenBoard, leakedBoard, cpuMemory)

        self.assertEqual(result, 0)
        self.assertEqual(hiddenBoard, [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ])
        self.assertEqual(leakedBoard, [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def test_ship_hit(self):
        hiddenBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        leakedBoard = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        cpuMemory = (1, 1)

        result = shootingfunction.checkHit(hiddenBoard, leakedBoard, cpuMemory)

        self.assertEqual(result, 1)
        self.assertEqual(hiddenBoard, [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def test_invalid_board(self):
        hiddenBoard = []
        leakedBoard = []
        cpuMemory = (1, 1)

        with self.assertRaises(IndexError):
            shootingfunction.checkHit(hiddenBoard, leakedBoard, cpuMemory)

    # @patch('builtins.input', side_effect=['K1', 'A11', 'A1'])
    # def test_playermanager_2(self, mock_input):
    #     result = playermanager(self.data, user1.getName(), leakedBoard2, hiddenBoard1, playerShips)
    #     self.assertEqual(result, None)

    # @patch('builtins.input', side_effect=['K1', 'A11', 'A1'])
    # def test_shooting_2(self, mock_input):
    #     result = shooting(self.data, self.gameMode, self.currentPlayer)
    #     self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
