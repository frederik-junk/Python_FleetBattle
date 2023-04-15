import unittest, main

#pylint: disable=C

class TestMain(unittest.TestCase):
    currentPlayer = 1

    def test_StartingUser(self):
        startingPlayer = main.selectStartingPlayer
        self.assertNotEqual(startingPlayer, 3)

if __name__ == '__main__':
    unittest.main()