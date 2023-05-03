# pylint: disable=C
from io import StringIO
import unittest
from unittest.mock import patch
from python_game import clear_console
import select_operations, os

class TestSelectOperations(unittest.TestCase):
    @patch('os.system')
    def test_clear_console(self, mock_system):
        mock_system.return_value = None
        clear_console()
        mock_system.assert_called_once_with("cls" if os.name == "nt" else "clear")

    @patch('builtins.input', side_effect=['j'])
    def test_load_game(self):
        data = {"storage_available": 1}
        expected_output = "Willkommen zurück, Ihre Daten konnten erfolgreich geladen werden.\nDas Spiel geht an gespeicherter Stelle weiter!\n"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = select_operations.load_request(data)
            self.assertEqual(result, True)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    @patch('builtins.input', side_effect=['n'])
    def test_new_game(self):
        data = {"storage_available": 0}
        expected_output = "Alles klar, das Spiel wird ohne Speicherdaten gestartet!\n"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = select_operations.load_request(data)
            self.assertEqual(result, False)
            self.assertEqual(fake_out.getvalue(), expected_output)

    # def test_game_mode_selection_one_player(self):
    #     data = {}
    #     input_str = '1\n'
    #     expected_output = "1-Spieler Modus."
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         with patch('builtins.input', side_effect=input_str):
    #             result = select_operations.game_mode_selection(data)
    #     self.assertEqual(data["game_mode"], 1)
    #     self.assertIn(expected_output, fake_out.getvalue())

    # def test_game_mode_selection_two_players(self):
    #     data = {}
    #     input_str = '2\nplayer1\nplayer2\n'
    #     expected_output = "2-Spieler Modus."
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         with patch('builtins.input', side_effect=input_str):
    #             result = select_operations.game_mode_selection(data)
    #     self.assertEqual(data["game_mode"], 2)
    #     self.assertIn(expected_output, fake_out.getvalue())

    # def test_game_mode_selection_wrong_input(self):
    #     data = {}
    #     input_str = '3\n2\n'
    #     expected_output = "Ihre Eingabe ist falsch."
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         with patch('builtins.input', side_effect=input_str):
    #             result = select_operations.game_mode_selection(data)
    #     self.assertEqual(data["game_mode"], 2)
    #     self.assertIn(expected_output, fake_out.getvalue())


if __name__ == "__main__":
    unittest.main()
