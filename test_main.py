import unittest, main

class TestMain(unittest.TestCase):
    currentPlayer = 1

    def test_StartingUser(self):
        startingPlayer = main.selectStartingPlayer
        self.assertNotEqual(startingPlayer, 3)