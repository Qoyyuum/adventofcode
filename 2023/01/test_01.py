import unittest

from trebuchet import Trebuchet

class TestTrebuchet(unittest.TestCase):
    def setUp(self):
        """Load the dataset"""
        self.trebuchet = Trebuchet("test_input.txt")

    def test_case_01(self):
        """Check if the test data returns the sum of 142"""
        actual = self.trebuchet.calculate_sum()
        expected = 142
        self.assertEqual(actual, expected)

    def tearDown(self):
        """Remove the dataset"""
        self.trebuchet = ""
