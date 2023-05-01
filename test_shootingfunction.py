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

    @patch('builtins.input', side_effect=['A1'])
    def test_shooting_1(self, mock_input):
        result = shootingfunction.shooting(data, self.gameMode, self.currentPlayer)
        self.assertEqual(result, None)

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
