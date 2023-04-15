import unittest
from shipmanager import *

class TestShipmanager(unittest.TestCase):

    def setUp(self):
        self.schlachtSchiff = Schlachtschiff(1)
        self.kreuzer = Kreuzer(2)

    def test_getName(self):
        self.assertEqual(self.schlachtSchiff.getName(), "Schlachtschiff")
        self.assertEqual(self.schlachtSchiff.getSize(), 5)
        self.assertEqual(self.kreuzer.getName(), "Kreuzer")
        self.assertEqual(self.kreuzer.getSize(), 4)

    def tearDown(self):
        del self.schlachtSchiff
        del self.kreuzer
