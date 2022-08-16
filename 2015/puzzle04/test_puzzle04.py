import unittest

from puzzle04 import AdventCoin

class TestPuzzle04(unittest.TestCase):

    def test01(self):
        """
        Given the secret key is abcdef,
        the answer is 609043.

        MD5 hash of abcdef609043 starts with
        000001dbbfa....
        And its the lowest number with 5 leading zeroes.
        """
        key = "abcdef"
        answer = "609043"
        
        a = AdventCoin(key)
        a.mine(5)
        expected = a.lowest_number

        self.assertEqual(expected, answer)

    def test02(self):
        """
        Given the secret key is pqrstuv,
        the answer is 1048970.

        MD5 hash of pqrstuv104870 starts with
        000006136ef....
        And its the lowest number with 5 leading zeroes.
        """
        key = "pqrstuv"
        answer = "1048970"
        
        a = AdventCoin(key)
        a.mine(5)
        expected = a.lowest_number

        self.assertEqual(expected, answer)
