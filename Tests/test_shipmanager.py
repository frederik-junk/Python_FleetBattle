import unittest
from shipmanager import *

#pylint: disable=C

class TestShipmanager(unittest.TestCase):

    def setUp(self):
        self.schlachtSchiff = Schlachtschiff(1)
        self.kreuzer = Kreuzer(2)

    def test_getName(self):
        self.assertEqual(self.schlachtSchiff.getName(), "Schlachtschiff")
        self.assertEqual(self.schlachtSchiff.getSize(), 5)
        self.assertEqual(self.kreuzer.getName(), "Kreuzer")
        self.assertEqual(self.kreuzer.getSize(), 4)

    def test_setPositon(self):
        self.schlachtSchiff.setPosition(7)
        self.assertEqual(self.schlachtSchiff.getPosition(),7)

    def test_hitOnShip(self):
        self.assertEqual(self.kreuzer.getDamageCounter(),0)
        self.kreuzer.hitOnShip()
        self.assertEqual(self.kreuzer.getDamageCounter(),1)

    def test_getSize(self):
        self.assertEqual(self.kreuzer.getSize(),4)

    def test_getPosition(self):
        self.assertEqual(self.schlachtSchiff.getPosition(),1)

    def tearDown(self):
        del self.schlachtSchiff
        del self.kreuzer

if __name__ == '__main__':
    unittest.main()