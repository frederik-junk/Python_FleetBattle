# pylint: disable=C
from io import StringIO
import json
import unittest, select_operations
from unittest.mock import patch
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



if __name__ == "__main__":
    unittest.main()
