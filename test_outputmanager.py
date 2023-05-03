import unittest
from unittest.mock import MagicMock, patch
from output_manager import *

# pylint: disable=C


class TestBattleEnd(unittest.TestCase):
    @patch("builtins.print")
    def test_battleEnd_computer_wins_1playermode(self, mock_print):
        # Set up test case
        user1 = MagicMock()
        user1.getName.return_value = "Spieler 1"
        user2 = MagicMock()
        user2.getName.return_value = "Computer"
        winID = 1
        gameMode = 1

        # Call the function
        battleEnd(winID, gameMode)

        # Check expected results
        # user1.getName.assert_called_once()
        # user2.getName.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[35mSpieler 1 hat das Spiel gewonnen. Spieler 2 versuche es doch noch einmal!\x1b[0m"
            ""
        )

    # Check if name gets returned correctly
    def test_getName(self):
        result = user1.getName()
        self.assertEqual(result, "Spieler 1")

    @patch("builtins.print")
    def test_battleEnd_player1_wins_2playermode(self, mock_print):
        # Set up test case
        user1 = MagicMock()
        user1.getName.return_value = "Spieler 1"
        user2 = MagicMock()
        user2.getName.return_value = "Spieler 2"
        winID = 1
        gameMode = 2

        # Call the function
        battleEnd(winID, gameMode)

        # Check expected results
        #     user1.getName.assert_called_once()
        #     user2.getName.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 1 du hast das Spiel gegen Spieler 2 gewonnen!\x1b[0m"
            ""
        )

    @patch("builtins.print")
    def test_battleEnd_player2_wins_2playermode(self, mock_print):
        # Set up test case
        user1 = MagicMock()
        user1.getName.return_value = "Spieler 1"
        user2 = MagicMock()
        user2.getName.return_value = "Spieler 2"
        winID = 2
        gameMode = 2

        # Call the function
        battleEnd(winID, gameMode)

        # Check expected results
        #     user1.getName.assert_called_once()
        #     user2.getName.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 2 du hast das Spiel gegen Spieler 1 gewonnen!\x1b[0m"
            ""
        )

    @patch("builtins.print")
    def test_battleEnd_player_wins_1playermode(self, mock_print):
        # Set up test case
        user1 = MagicMock()
        user1.getName.return_value = "Computer"
        user2 = MagicMock()
        user2.getName.return_value = "Spieler 2"
        winID = 2
        gameMode = 1

        # Call the function
        battleEnd(winID, gameMode)

        # Check expected results
        #     user1.getName.assert_called_once()
        #     user2.getName.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 2 du hast das Spiel gegen den Computer gewonnen!\x1b[0m"
            ""
        )


if __name__ == "__main__":
    unittest.main()
