import unittest

from game import Bag


class TestCubeGame(unittest.TestCase):
    def setUp(self):
        """Load the Test dataset"""
        self.bag = Bag("test_input.txt")
        condition = {"red": 12, "green": 13, "blue": 14}
        self.bag.get_possible_games(condition)

    def test_case_01(self):
        """Checks the bag contains 12 red cubes, 13 green cubes and 14 blue cubes
        And returns the game ID list of 1, 2 and 5"""
        actual = self.bag.possible_games
        expected = [1, 2, 5]
        self.assertEqual(actual, expected)

    def test_case_02(self):
        """Sum of total possible games is 8"""
        actual = self.bag.total_possible_games()
        expected = 8
        self.assertEqual(actual, expected)

    def test_case_03(self):
        """Total power set of minimum cubes in all games is 2286"""
        actual = self.bag.get_max_cubes_per_color()
        expected = 2286
        self.assertEqual(actual, expected)
