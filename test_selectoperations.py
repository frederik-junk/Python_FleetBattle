import unittest
from random import randint
from unittest.mock import MagicMock, patch
from selectoperations import *

class TestStartingPlayerSelection(unittest.TestCase):
    
    @patch('builtins.print')
    def test_selectStartingPlayer_player2_starts(self, mock_print):
        # Mock outputmanager and set up test case
        outputmanager = MagicMock()
        outputmanager.user2.getName.return_value = "Player2"
        mode = "2"
        
        # Call the function
        selectStartingPlayer(mode)
        
        # Check expected result
        mock_print.assert_called_with("Spieler 1 darf das Spiel beginnen und ist an der Reihe!")
        mock_print.assert_called_with("Spieler 2 darf das Spiel beginnen und ist an der Reihe!")
    
    # @patch('builtins.print')
    # @patch('random.randint', return_value=1)
    # def test_selectStartingPlayer_player1_starts(self, mock_randint, mock_print):
    #     # Mock outputmanager and set up test case
    #     outputmanager = MagicMock()
    #     outputmanager.user1.getName.return_value = "Player1"
    #     mode = "any_mode"
        
    #     # Call the function
    #     selectStartingPlayer(mode)
        
    #     # Check expected results
    #     mock_print.assert_called_once_with("Es wird zufällig bestimmt wer beginnt...")
    #     outputmanager.user1.getName.assert_called_once()
    #     mock_print.assert_called_with("Player1 darf das Spiel beginnen und ist an der Reihe!")
    
    # @patch('builtins.print')
    # @patch('random.randint', return_value=1)
    # def test_selectStartingPlayer_computer_starts(self, mock_randint, mock_print):
    #     # Mock outputmanager and set up test case
    #     outputmanager = MagicMock()
    #     outputmanager.user1.getName.return_value = "Computer"
    #     mode = "1"
        
    #     # Call the function
    #     selectStartingPlayer(mode)
        
    #     # Check expected results
    #     mock_print.assert_called_once_with("Es wird zufällig bestimmt wer beginnt...")
    #     outputmanager.user1.getName.assert_called_once()
    #     mock_print.assert_called_with("Computerccccccc darf das Spiel beginnen und ist an der Reihe!")
    
if __name__ == '__main__':
    unittest.main()
