import unittest
from oponent import *

class TestOpponent(unittest.TestCase):

    def setUp(self):
        self.oschlachtschiff = schlachtschiff1
        self.leakedBoard = [
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,2,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,1,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,3,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0]
                            ]
        self.hiddenBoard = [
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,2,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,1,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,1,0,0,0,0,0,0,0],
                            [0,0,0,3,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0]
                            ]
        row = 2
        column = 4

    def test_opponentGetPosition(self):
        self.assertNotEqual(self.oschlachtschiff.getPosition(),0)

    def test_checkHit(self):
        self.assertEqual(checkHit(self.hiddenBoard, self.leakedBoard,1,1),1)
        self.assertEqual(checkHit(self.hiddenBoard, self.leakedBoard, 5,6),0)

    # def test_opponentAction(self):
    #     self.assertEqual(opponentAction(),1)

    def tearDown(self):
        del self.oschlachtschiff
        del self.leakedBoard
        del self.hiddenBoard

if __name__ == "__main__":
    unittest.main()


    
