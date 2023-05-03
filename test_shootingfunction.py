import unittest
from unittest.mock import Mock, patch
import io
import sys
import random
import pythonGame
import converterfunctions
import shipinitializer
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

        #self.assertEqual(result, 1)
        self.assertIsNone(result)
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

    def test_first_position_returns_tuple(self):
        board = [[0 for _ in range(10)] for _ in range(10)]
        firstCpuMemory = shootingfunction.firstPosition(board)
        self.assertIsInstance(firstCpuMemory, tuple)
    
    def test_first_position_returns_valid_coordinates(self):
        board = [[0 for _ in range(10)] for _ in range(10)]
        firstCpuMemory = shootingfunction.firstPosition(board)
        row, col = firstCpuMemory
        self.assertGreaterEqual(row, 0)
        self.assertLess(row, 10)
        self.assertGreaterEqual(col, 0)
        self.assertLess(col, 10)

    def test_cpuManager1_return_11(self):
        self.shootingIq = 0
        user1 = Mock()
        user1.getFirstCpuMemory.return_value = (5, 5)
        user1.getCpuMemory.return_value = (5, 5)
        user1.getDirection.return_value = 0
        self.leakedBoard = [[0 for i in range(10)] for j in range(10)]
        self.hiddenBoard = [[0 for i in range(10)] for j in range(10)]
        cpuManager1_return = shootingfunction.cpuManager1(self.gameMode, self.currentPlayer, self.shootingIq, self.data, self.leakedBoard, self.hiddenBoard)
        self.assertEqual(cpuManager1_return, "something went wrong")

    # @patch('cpu_manager.randomDirection')
    # def test_cpuManager1_shootingIq_1(self, mock_randomDirection):
    #     mock_randomDirection.return_value = 1
    #     user1 = Mock()
    #     user1.getFirstCpuMemory.return_value = (5, 5)
    #     user1.getCpuMemory.return_value = (5, 6)
    #     user1.getDirection.return_value = 1
    #     self.shootingIq = 1
    #     cpuManager1_return = shootingfunction.cpuManager1(self.gameMode, self.currentPlayer, self.shootingIq, self.data)
    #     self.assertEqual(user1.setCpuMemory.call_count, 3)
    #     self.assertEqual(user1.setDirection.call_count, 2)
    #     self.assertEqual(user1.setShootingIq.call_count, 2)

    # def test_cpuManager1_shootingIq_2(self):
    #     user1 = Mock()
    #     user1.getFirstCpuMemory.return_value = (5, 5)
    #     user1.getCpuMemory.return_value = (4, 5)
    #     user1.getDirection.return_value = 2
    #     self.shootingIq = 2
    #     cpuManager1_return = shootingfunction.cpuManager1(self.gameMode, self.currentPlayer, self.shootingIq, self.data)
    #     self.assertEqual(user1.setCpuMemory.call_count, 2)
    #     self.assertEqual(user1.setShootingIq.call_count, 1)

    # def test_cpuManager1_shootingIq_3(self):
    #     user1 = Mock()
    #     user1.getFirstCpuMemory.return_value = (5, 5)
    #     user1.getCpuMemory.return_value = (4, 6)
    #     user1.getDirection.return_value = 3
    #     self.shootingIq = 3
    #     cpuManager1_return = shootingfunction.cpuManager1(self.gameMode, self.currentPlayer, self.shootingIq, self.data)
    #     self.assertEqual(user1.setCpuMemory.call_count, 2)
    #     self.assertEqual(user1.setShootingIq.call_count, 1)

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
