import unittest

from day01 import Elf

class TestCalories(unittest.TestCase):
    def setUp(self):
        """Load test dataset"""
        with open("test_input.txt", 'r') as test_input_data:
            self.data = test_input_data.readlines()



    def test_first_elf(self):
        """
        Expected to get a total calories of 6000 for the first elf.
        """
        ...

    def test_second_elf(self):
        """
        Expected to get a total calories of 4000 for the 2nd elf.
        """
        ...

    def test_third_elf(self):
        """
        Expected to get a total calories of 11000 for the 3rd elf.
        """
        ...

    def test_fourth_elf(self):
        """
        Expected to get a total calories of 24000 for the 4th elf.
        """
        ...

    def test_fifth_elf(self):
        """
        Expected to get a total calories of 10000 for the 5th elf.
        """
        ...
