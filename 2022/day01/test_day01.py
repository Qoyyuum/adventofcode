import unittest

from day01 import Elf, Elves

class TestCalories(unittest.TestCase):
    def setUp(self):
        """Load test dataset"""
        self.elves = Elves("test_input.txt")

    def test_elves_list(self):
        """
        Checks if the test list returns 5 elves
        """
        self.assertEqual(len(self.elves), 5)

    def test_first_elf(self):
        """
        Expected to get a total calories of 6000 for the first elf.
        """
        self.assertEqual(self.elves[0].calories, 6000)

    def test_second_elf(self):
        """
        Expected to get a total calories of 4000 for the 2nd elf.
        """
        self.assertEqual(self.elves[1].calories, 4000)

    def test_third_elf(self):
        """
        Expected to get a total calories of 11000 for the 3rd elf.
        """
        self.assertEqual(self.elves[2].calories, 11000)

    def test_fourth_elf(self):
        """
        Expected to get a total calories of 24000 for the 4th elf.
        """
        self.assertEqual(self.elves[3].calories, 24000)

    def test_fifth_elf(self):
        """
        Expected to get a total calories of 10000 for the 5th elf.
        """
        print(self.elves)
        print(len(self.elves))
        self.assertEqual(self.elves[4].calories, 10000)
