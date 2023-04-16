import unittest
import random
from unittest.mock import MagicMock, patch
from selectoperations import *

class TestStartingPlayerSelection(unittest.TestCase):
    
    @patch('builtins.print')
    def test_selectStartingPlayer_player2_starts(self, mock_print):
        # Mock outputmanager and set up test case
        mode = 1
        outputmanager = MagicMock()
        outputmanager.user2.getName.return_value = "Spieler 2"
        startingPlayer = MagicMock()
        startingPlayer.return_value = 2

        # Call the function with the mocked startingPlayer
        with patch('selectoperations.randint', startingPlayer):
            selectStartingPlayer(mode)
        
        # Check expected result
        mock_print.assert_called_with("Spieler 2 darf das Spiel beginnen und ist an der Reihe!")

    @patch('builtins.print')
    def test_selectStartingPlayer_start_message(self, mock_print):
        # Mock outputmanager and set up test case
        mode = 1
        outputmanager = MagicMock()
        outputmanager.user2.getName.return_value = "Spieler 2"
        startingPlayer = MagicMock()
        startingPlayer.return_value = 1
        
        # Call the function with the mocked startingPlayer
        with patch('selectoperations.randint', startingPlayer):
            selectStartingPlayer(mode)
        
        # Check expected result
        mock_print.assert_called_with("Spieler 1 darf das Spiel beginnen und ist an der Reihe!")
    
    @patch('builtins.print')
    @patch('random.randint', return_value=1)
    def test_selectStartingPlayer_player1_starts(self, mock_randint, mock_print):
        # Mock outputmanager and set up test case
        outputmanager = MagicMock()
        outputmanager.user1.getName.return_value = "Spieler 1"
        mode = "2"
        startingPlayer = MagicMock()
        startingPlayer.return_value = 1
        
        # Call the function
        with patch('selectoperations.randint', startingPlayer):
            selectStartingPlayer(mode)
        
        # Check expected results
        mock_print.assert_called_with("Spieler 1 darf das Spiel beginnen und ist an der Reihe!")
    
    @patch('builtins.print')
    @patch('random.randint', return_value=1)
    def test_selectStartingPlayer_computer_starts(self, mock_randint, mock_print):
        # Mock outputmanager and set up test case
        outputmanager = MagicMock()
        outputmanager.user1.getName.return_value = "Computer"
        startingPlayer = MagicMock()
        startingPlayer.return_value = 1
        mode = "1"
        
        # Call the function
        with patch('selectoperations.randint', startingPlayer):
            selectStartingPlayer(mode)
        
        # Check expected results
        mock_print.assert_called_with("Spieler 1ccccccc darf das Spiel beginnen und ist an der Reihe!")
    
if __name__ == '__main__':
    unittest.main()
