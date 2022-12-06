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

    def test_2(self):
        """
        From the test input, there are 4 overlapping assignment pairs.
        """
        count = 0
        for test_pair in self.test_data:
            section = Section(test_pair)
            section.split()
            if section.is_overlapped:
                count += 1
        expected = 4
        self.assertEqual(count, expected)

    def test_expand_int_range(self):
        """
        Expand from 1-10 to [1,2,3,4,5,6,7,8,9,10]
        """
        expected = [1,2,3,4,5,6,7,8,9,10]
        start = 1
        end = 10
        self.assertEqual(Section.expand_int_range(start, end), expected)

if __name__ == "__main__":
    unittest.main()
