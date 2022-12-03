import unittest

from day03 import Rucksack

class TestRucksack(unittest.TestCase):
    def setUp(self):
        with open('test_input.txt', 'r') as file:
            self.data = file.read().strip()
            print(self.data)

    def test_part_1(self):
        "Total sum is 157"
        ...

if __name__ == "__main__":
    unittest.main()
