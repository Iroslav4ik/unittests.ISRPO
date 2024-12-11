import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()