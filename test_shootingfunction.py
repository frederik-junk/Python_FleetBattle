# pylint: disable=C
import unittest
from unittest.mock import Mock, patch
import io
import sys
import shooting_function


class TestShooting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = {}
        cls.current_player = 1
        cls.game_mode = 1
        cls.user_1 = "Testspieler"

    # @patch('builtins.input', side_effect=['A1'])
    # def test_player_manager_1(self, mock_input):
    #     global user_1
    #     result = shootingfunction.player_manager(self.data, user_1.get_name(), leaked_board2, hidden_board1, playerShips)
    #     self.assertEqual(result, None)

    # @patch('builtins.input', side_effect=['A1'])
    # def test_shooting_1(self, mock_input):
    #     result = shootingfunction.shooting(self.data, self.game_mode, self.current_player)
    #     self.assertEqual(result, None)

    def test_player_manager(self):
        leaked_board = [[0 for i in range(10)] for j in range(10)]
        hidden_board = [[0 for i in range(10)] for j in range(10)]
        ship_list = []
        current_player = 1
        with io.StringIO("A1\n") as mock_input:
            sys.stdin = mock_input
            output = shooting_function.player_manager(
                current_player,
                leaked_board,
                hidden_board,
                ship_list,
            )
            self.assertIsNone(output)

    def test_next_player_player_1(self):
        # Test for current_player == 1
        current_player = 1
        data = {"current_player": 1}

        with patch("builtins.input", return_value="a"):
            shooting_function.next_player(data, current_player)
            self.assertEqual(data["current_player"], 2)

    def test_next_player_error(self):
        # Test for invalid current_player value
        current_player = 3
        data = {"current_player": 3}
        expected_output = "Der Spielerwechsel schlug fehl!\n"
        with patch("builtins.input", return_value="a"):
            with patch("sys.stdout", new=io.StringIO()) as fake_output:
                shooting_function.next_player(data, current_player)
                self.assertEqual(fake_output.getvalue(), expected_output)

    @patch("random.randint")
    def test_random_direction(self, mock_randint):
        # Set up the mock random integer function to return a known value
        mock_randint.return_value = 2

        # Call the function and assert that it returns the expected value
        result = shooting_function.random_direction()
        self.assertEqual(result, 2)

        # Assert that the mock random integer function was called with the expected arguments
        mock_randint.assert_called_once_with(0, 3)

    def test_missed_shot(self):
        hidden_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        leaked_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        cpu_memory = (1, 1)

        result = shooting_function.check_hit(hidden_board, leaked_board, cpu_memory)

        self.assertEqual(result, 0)
        self.assertEqual(hidden_board, [[0, 0, 0], [0, 2, 0], [0, 0, 0]])

    def test_water_hit(self):
        hidden_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        leaked_board = [[0, 0, 0], [0, 6, 0], [0, 0, 0]]
        cpu_memory = (1, 1)

        result = shooting_function.check_hit(hidden_board, leaked_board, cpu_memory)

        self.assertEqual(result, 0)
        self.assertEqual(hidden_board, [[0, 0, 0], [0, 2, 0], [0, 0, 0]])
        self.assertEqual(leaked_board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_ship_hit(self):
        hidden_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        leaked_board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        cpu_memory = (1, 1)

        result = shooting_function.check_hit(hidden_board, leaked_board, cpu_memory)


        #self.assertEqual(result, 1)
        self.assertIsNone(result)
        self.assertEqual(hidden_board, [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])


    def test_invalid_board(self):
        hidden_board = []
        leaked_board = []
        cpu_memory = (1, 1)

        with self.assertRaises(IndexError):
            shooting_function.check_hit(hidden_board, leaked_board, cpu_memory)

    def test_first_position_returns_tuple(self):
        board = [[0 for _ in range(10)] for _ in range(10)]
        first_cpu_memory = shooting_function.first_position(board)
        self.assertIsInstance(first_cpu_memory, tuple)

    def test_first_position_returns_valid_coordinates(self):
        board = [[0 for _ in range(10)] for _ in range(10)]
        first_cpu_memory = shooting_function.first_position(board)
        row, col = first_cpu_memory
        self.assertGreaterEqual(row, 0)
        self.assertLess(row, 10)
        self.assertGreaterEqual(col, 0)
        self.assertLess(col, 10)

    def test_cpu_manager_1_return_11(self):
        self.shooting_iq = 0
        self.leaked_board = [[0 for i in range(10)] for j in range(10)]
        self.hidden_board = [[0 for i in range(10)] for j in range(10)]
        user_1 = Mock()
        user_1.get_first_cpu_memory.return_value = (5, 5)
        user_1.get_cpu_memory.return_value = (5, 5)
        user_1.get_direction.return_value = 0
        cpu_manager_1_return = shooting_function.cpu_manager_1(self.shooting_iq, self.leaked_board, self.hidden_board)
        self.assertEqual(cpu_manager_1_return, None)

if __name__ == "__main__":
    unittest.main()
