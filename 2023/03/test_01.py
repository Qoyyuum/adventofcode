import unittest


from gondola import Engine


class TestGearRatios(unittest.TestCase):
    def setUp(self):
        """Load the Test dataset"""
        self.engine = Engine("test_input.txt")
        self.engine.find_part_numbers()

    def test_case_01(self):
        """Make sure that 114 and 58 is not in the list of part numbers"""
        actual = self.engine.part_numbers
        expected = sorted([467, 35, 633, 617, 592, 755, 664, 598])
        self.assertEqual(actual, expected)
        self.assertNotIn(114, actual)
        self.assertNotIn(58, actual)

    def test_case_02(self):
        """Sum of the part numbers is 4361"""
        actual = sum(self.engine.part_numbers)
        expected = 4361
        self.assertEqual(actual, expected)
