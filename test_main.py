# pylint: disable=C
import unittest, select_operations

class TestMain(unittest.TestCase):
    current_player = 1

    def test_StartingUser(self):
        starting_player = select_operations.select_starting_player
        self.assertNotEqual(starting_player, 3)


if __name__ == "__main__":
    unittest.main()
