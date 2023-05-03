# pylint: disable=C
from io import StringIO
import json
import unittest, select_operations
from unittest.mock import mock_open, patch
from main import main

class TestMain(unittest.TestCase):
    current_player = 1

    def test_StartingUser(self):
        starting_player = select_operations.select_starting_player
        self.assertNotEqual(starting_player, 3)

    @patch('builtins.input', return_value='2')
    def test_main_should_load_game_false(self, mock_input):
        data = {
                "game_mode": "",
                "board_1": [],
                "board_2": [],
                "storage_available": 1,
                "current_player": "1"
            }

        with patch('sys.stdout', new=StringIO()) as fake_output:
            select_operations.load_request = lambda data: False
            main()
            output = fake_output.getvalue().strip()

            self.assertIn("Spieler 1 beginnt das Spiel", output)
            self.assertIn("Spieler 2 hat gewonnen", output)



if __name__ == "__main__":
    unittest.main()
