import unittest

from day02 import RPS

class TestRPG(unittest.TestCase):
    """
    Opponent options:
    A = Rock
    B = Paper
    C = Scissors

    My options:
    Y = Paper
    X = Rock
    Z = Scissors

    Rock > Paper > Scissors

    Calculation for each win is determined as follows:
    1. Score of a single round is the score of the shape selected. i.e.
        1 for Rock
        2 for Paper
        3 for Scissors
    2. Plus the score for the outcome of the round (0 for lost, 3 for draw and 6 for won)
    """
    
    def setUp(self):
        self.strategy = "test_input.txt"

    def test01(self):
        """
        Expected total score 15 in part 1
        """
        game = RPS()
        score = game.play(self.strategy, True)
        expected = 15
        self.assertEqual(score, expected)

    def test02(self):
        """
        Expected total score 12 in part 2
        """
        game = RPS()
        score = game.play(self.strategy, False)
        expected = 12
        self.assertEqual(score, expected)

if __name__ == "__main__":
    unittest.main()
