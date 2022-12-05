import unittest

from day04 import Section

class TestSection(unittest.TestCase):
    def setUp(self):
        """
        Load test inputs
        """
        with open('test_input.txt', 'r') as test_file:
            self.test_data = test_file.readlines()

    def test_1(self):
        """
        From the test input, get 2 pairs fully contained other.
        """
        fully_contained_pairs_list = []
        for test_pair in self.test_data:
            section = Section(test_pair)
            section.split()
            section.check_fully_contained()
            if section.fully_contained:
                fully_contained_pairs_list.append(section.fully_contained)
        expected = 2
        self.assertEqual(len(fully_contained_pairs_list), expected)

if __name__ == "__main__":
    unittest.main()
