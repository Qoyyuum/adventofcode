import unittest
from puzzle02 import Puzzle02

class TestPuzzle02(unittest.TestCase):
    def test_total_square_feet01(self):
        """
        Test to get the total square feet,
        given length, width and height.

        @result = integer
        """
        l = 2
        w = 3
        h = 4
        wrapping_paper = 52
        extra_paper = 6

        p = Puzzle02(l, w, h)
        p.calculate_total_square_feet()
        self.assertEqual(p.wrapping_paper, wrapping_paper)
        self.assertEqual(p.extra_paper, extra_paper)

    def test_total_square_feet02(self):
        """
        Test to get the total square feet,
        given length, width and height.

        @result = integer
        """
        l = 1
        w = 1
        h = 10 
        wrapping_paper = 42
        extra_paper = 1

        p = Puzzle02(l, w, h)
        p.calculate_total_square_feet()
        self.assertEqual(p.wrapping_paper, wrapping_paper)
        self.assertEqual(p.extra_paper, extra_paper)

    def test_ribbon_length01(self):
        """
        Test to get the wrapping ribbon length and
        get the bow ribbon length.

        @result = integer
        """
        l = 2
        w = 3
        h = 4
        wrapping_ribbon = 10
        bow_ribbon = 24 
        total_ribbon = wrapping_ribbon + bow_ribbon

        p = Puzzle02(l, w, h)
        total = p.calculate_total_ribbon_length()
        self.assertEqual(p.wrapping_ribbon, wrapping_ribbon)
        self.assertEqual(p.bow_ribbon, bow_ribbon)
        self.assertEqual(total, total_ribbon)


    def test_ribbon_length02(self):
        """
        Test to get the wrapping ribbon length and
        get the bow ribbon length.

        @result = integer
        """
        l = 1
        w = 1
        h = 10
        wrapping_ribbon = 4
        bow_ribbon = 10
        total_ribbon = wrapping_ribbon + bow_ribbon

        p = Puzzle02(l, w, h)
        total = p.calculate_total_ribbon_length()
        self.assertEqual(p.wrapping_ribbon, wrapping_ribbon)
        self.assertEqual(p.bow_ribbon, bow_ribbon)
        self.assertEqual(total, total_ribbon)
