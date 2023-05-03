import unittest, select_operations

# pylint: disable=C


class TestMain(unittest.TestCase):
    currentPlayer = 1

    def test_StartingUser(self):
        startingPlayer = select_operations.selectStartingPlayer
        self.assertNotEqual(startingPlayer, 3)


if __name__ == "__main__":
    unittest.main()
