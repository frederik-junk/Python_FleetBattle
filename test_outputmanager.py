# pylint: disable=C
import unittest
from unittest.mock import MagicMock, patch
import output_manager

class TestBattleEnd(unittest.TestCase):
    @patch("builtins.print")
    def test_battle_end_computer_wins_1playermode(self, mock_print):
        # Set up test case
        user_1 = MagicMock()
        user_1.get_name.return_value = "Spieler 1"
        user_2 = MagicMock()
        user_2.get_name.return_value = "Computer"
        win_id = 1
        game_mode = 1

        # Call the function
        output_manager.battle_end(win_id, game_mode)

        # Check expected results
        # user_1.get_name.assert_called_once()
        # user_2.get_name.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[35mSpieler 1 hat das Spiel gewonnen. Spieler 2 versuche es doch noch einmal!\x1b[0m"
            ""
        )

    # Check if name gets returned correctly
    def test_get_name(self):
        user_1 = MagicMock()
        user_1.get_name.return_value = "Spieler 1"
        result = user_1.get_name()
        self.assertEqual(result, "Spieler 1")

    @patch("builtins.print")
    def test_battle_end_player1_wins_2playermode(self, mock_print):
        # Set up test case
        user_1 = MagicMock()
        user_1.get_name.return_value = "Spieler 1"
        user_2 = MagicMock()
        user_2.get_name.return_value = "Spieler 2"
        win_id = 1
        game_mode = 2

        # Call the function
        output_manager.battle_end(win_id, game_mode)

        # Check expected results
        #     user_1.get_name.assert_called_once()
        #     user_2.get_name.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 1 du hast das Spiel gegen Spieler 2 gewonnen!\x1b[0m"
            ""
        )

    @patch("builtins.print")
    def test_battle_end_player2_wins_2playermode(self, mock_print):
        # Set up test case
        user_1 = MagicMock()
        user_1.get_name.return_value = "Spieler 1"
        user_2 = MagicMock()
        user_2.get_name.return_value = "Spieler 2"
        win_id = 2
        game_mode = 2

        # Call the function
        output_manager.battle_end(win_id, game_mode)

        # Check expected results
        #     user_1.get_name.assert_called_once()
        #     user_2.get_name.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 2 du hast das Spiel gegen Spieler 1 gewonnen!\x1b[0m"
            ""
        )

    @patch("builtins.print")
    def test_battle_end_player_wins_1playermode(self, mock_print):
        # Set up test case
        user_1 = MagicMock()
        user_1.get_name.return_value = "Computer"
        user_2 = MagicMock()
        user_2.get_name.return_value = "Spieler 2"
        win_id = 2
        game_mode = 1

        # Call the function
        output_manager.battle_end(win_id, game_mode)

        # Check expected results
        #     user_1.get_name.assert_called_once()
        #     user_2.get_name.assert_called_once()
        mock_print.assert_called_with(
            ""
            "\x1b[32mHerzlichen Glueckwunsch Spieler 2 du hast das Spiel gegen den Computer gewonnen!\x1b[0m"
            ""
        )


if __name__ == "__main__":
    unittest.main()
