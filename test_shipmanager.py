# pylint: disable=C
import unittest
import ship_manager

class TestShipmanager(unittest.TestCase):
    def setUp(self):
        self.schlachtSchiff = ship_manager.Schlachtschiff(1, 4)
        self.kreuzer = ship_manager.Kreuzer(2, 2)

    def test_get_name(self):
        self.assertEqual(self.schlachtSchiff.get_name(), "Schlachtschiff(1x)")
        self.assertEqual(self.schlachtSchiff.get_size(), 5)
        self.assertEqual(self.kreuzer.get_name(), "Kreuzer(2x)")
        self.assertEqual(self.kreuzer.get_size(), 4)

    def test_setPositon(self):
        self.schlachtSchiff.set_position(7)
        self.assertEqual(self.schlachtSchiff.get_position(), 7)

    def test_hitOnShip(self):
        self.assertEqual(self.kreuzer.get_damage_counter(), 0)
        self.kreuzer.hitOnShip()
        self.assertEqual(self.kreuzer.get_damage_counter(), 1)

    def test_get_size(self):
        self.assertEqual(self.kreuzer.get_size(), 4)

    def test_get_position(self):
        self.assertEqual(self.schlachtSchiff.get_position(), 1)

    def tearDown(self):
        del self.schlachtSchiff
        del self.kreuzer


if __name__ == "__main__":
    unittest.main()
