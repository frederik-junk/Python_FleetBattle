# pylint: disable=C
import json
import unittest, select_operations
from unittest.mock import mock_open, patch
from main import main

class TestMain(unittest.TestCase):
    current_player = 1

    def test_StartingUser(self):
        starting_player = select_operations.select_starting_player
        self.assertNotEqual(starting_player, 3)

    # @patch('output_manager.welcome_user')
    # @patch('select_operations.load_request')
    # @patch('python_game.board_loader')
    # @patch('memory_manager.load_data')
    # @patch('shooting_function.shooting')
    # @patch('shooting_function.next_player')
    # @patch('python_game.board_reset')
    # @patch('output_manager.battle_end')
    # def test_main_load_game(self, mock_battle_end, mock_board_reset, mock_next_player, mock_shooting, mock_load_data, mock_board_loader, mock_load_request, mock_welcome_user):
    #     data = {
    #         "game_mode": "1",
    #         "current_player": 1,
    #         "storage_available": 1
    #     }
    #     mock_load_request.return_value = True
    #     with patch('builtins.open', mock_open(read_data=json.dumps(data))):
    #         main()
    #     mock_welcome_user.assert_called_once()
    #     mock_load_request.assert_called_once_with(data)
    #     mock_board_loader.assert_called_once_with(data, True)
    #     mock_load_data.assert_called_once_with(data, "1")
    #     mock_shooting.assert_called()
    #     mock_next_player.assert_called()
    #     mock_board_reset.assert_called_once_with(data)
    #     mock_battle_end.assert_called_once()

    # @patch('output_manager.welcome_user')
    # @patch('select_operations.load_request')
    # @patch('python_game.board_loader')
    # @patch('select_operations.game_mode_selection')
    # @patch('select_operations.select_starting_player')
    # @patch('shooting_function.shooting')
    # @patch('shooting_function.next_player')
    # @patch('python_game.board_reset')
    # @patch('output_manager.battle_end')
    # def test_main_new_game(self, mock_battle_end, mock_board_reset, mock_next_player, mock_shooting, mock_select_starting_player, mock_game_mode_selection, mock_board_loader, mock_load_request, mock_welcome_user):
    #     data = {
    #         "game_mode": "",
    #         "current_player": "",
    #         "storage_available": 0
    #     }
    #     mock_load_request.return_value = False
    #     mock_game_mode_selection.return_value = "1"
    #     mock_select_starting_player.return_value = 1
    #     with patch('builtins.open', mock_open(read_data=json.dumps(data))):
    #         main()
    #     mock_welcome_user.assert_called_once()
    #     mock_load_request.assert_called_once_with(data)
    #     mock_board_loader.assert_called_once_with(data, False)
    #     mock_game_mode_selection.assert_called_once_with(data)
    #     mock_select_starting_player.assert_called_once_with(data)
    #     mock_shooting.assert_called()
    #     mock_next_player.assert_called()
    #     mock_board_reset.assert_called_once_with(data)
    #     mock_battle_end.assert_called_once()


if __name__ == "__main__":
    unittest.main()
