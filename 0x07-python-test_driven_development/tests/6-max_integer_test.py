#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_0(self):
        """Test"""
        self.assertEqual(max_integer([4, 2, 3]), 4)

    def test_1(self):
        """Test"""
        self.assertEqual(max_integer([4.5, 4.009, 2]), 4.5)

    def test_2(self):
        """Test"""
        self.assertEqual(max_integer([]), None)

    def test_3(self):
        """Test"""
        self.assertEqual(max_integer([3, float('inf'), 2]), float('inf'))

    def test_4(self):
        """Test"""
        self.assertEqual(max_integer([0.2, float('NaN'), 0.02]), 0.2)

    def test_5(self):
        """Test"""
        self.assertEqual(max_integer([-5.5, -1, -0.0001]), -0.0001)

    def test_6(self):
        """Test"""
        self.assertEqual(max_integer([47]), 47)


if __name__ == "__main__":
    unittest.main()
