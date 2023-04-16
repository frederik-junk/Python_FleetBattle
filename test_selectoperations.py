import unittest
from selectoperations import *

class TestSelectOperations(unittest.TestCase):

    def setUp(self):
        gameMode = 1
        startingPlayer = 2
    
    def test_selectStartinPlayer(self):
        self.assertEqual(selectStartingPlayer(self.gameMode),1)