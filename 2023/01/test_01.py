import unittest

from trebuchet import Trebuchet

class TestTrebuchet(unittest.TestCase):
    def test_case_01(self):
        """Check if the test data returns the sum of 142"""
        self.trebuchet = Trebuchet("test_input.txt")
        actual = self.trebuchet.calculate_sum()
        expected = 142
        self.assertEqual(actual, expected)

    def test_case_02(self):
        """Check if the test data returns the sum of 281"""
        self.trebuchet = Trebuchet("test_input_2.txt")
        actual = self.trebuchet.calculate_sum()
        expected = 281
        self.assertEqual(actual, expected)
