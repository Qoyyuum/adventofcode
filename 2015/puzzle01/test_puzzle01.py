import unittest
from puzzle01 import Puzzle01 

class TestPuzzle01(unittest.TestCase):
    def test_get_floors(self):
        """
        Test to count the total of open brackets subtract
        the total of closed brackets and return the result
        
        @result = integer
        """
        test = '(())'
        result = 0
        p = Puzzle01(test)
        p.count_brackets()
        self.assertEqual(p.floor, result)

    def test_get_first_basement_entry(self):
        """
        Test to get the position when entering the basement.
        i.e. As soon as the position is -1
        
        @result = integer
        """
        test = '()())'
        result = 5
        p = Puzzle01(test)
        p.count_brackets()
        self.assertEqual(p.basement_position, result)


if __name__ == '__main__':
    unittest.main()
