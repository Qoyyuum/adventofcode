import unittest

from puzzle05 import Name

class TestPuzzle05(unittest.TestCase):
    def test_three_vowels01(self):
        """
        It has at least 3 vowels

        @result = 3
        """
        test = 'aei'
        expected = 3
        n = Name(test)
        n.check_vowels()
        self.assertEqual(n.vowels, expected)

    def test_three_vowels02(self):
        """
        It has at least 3 vowels

        @result = 3
        """
        test = 'xazegov'
        expected = 3
        n = Name(test)
        n.check_vowels()
        self.assertEqual(n.vowels, expected)

    def test_three_vowels03(self):
        """
        It has at least 3 vowels

        @result = 3
        """
        test = 'aeiouaeiouaeiou'
        expected = 15
        n = Name(test)
        n.check_vowels()
        self.assertEqual(n.vowels, expected)

    def test_repeatable_letter01(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'xx'
        expected = True
        n = Name(test)
        n.check_repeatable_letter()
        self.assertEqual(n.repeatedletter, expected)

    def test_repeatable_letter02(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'abcdde'
        expected = True
        n = Name(test)
        n.check_repeatable_letter()
        self.assertEqual(n.repeatedletter, expected)

    def test_repeatable_letter03(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'aabbccdd'
        expected = True
        n = Name(test)
        n.check_repeatable_letter()
        self.assertEqual(n.repeatedletter, expected)
    
    def test_forbidden_strings01(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'ab'
        expected = True
        n = Name(test)
        n.check_forbidden_strings()
        self.assertEqual(n.forbidden, expected)
    
    def test_forbidden_strings02(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'cd'
        expected = True
        n = Name(test)
        n.check_forbidden_strings()
        self.assertEqual(n.forbidden, expected)
    
    def test_forbidden_strings03(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'pq'
        expected = True
        n = Name(test)
        n.check_forbidden_strings()
        self.assertEqual(n.forbidden, expected)

    def test_forbidden_strings04(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'xy'
        expected = True
        n = Name(test)
        n.check_forbidden_strings()
        self.assertEqual(n.forbidden, expected)

    def test_nice01(self):
        """
        Check if its nice
        """
        test = 'ugknbfddgicrmopn'
        expected = True
        n = Name(test)
        n.is_nice()
        self.assertEqual(n.nice, expected)

    def test_nice02(self):
        """
        Check if its nice
        """
        test = 'aaa'
        expected = True
        n = Name(test)
        n.is_nice()
        self.assertEqual(n.nice, expected)


    def test_nice03(self):
        """
        Check if its naughty
        """
        test = 'jchzalrnumimnmhp'
        expected = False
        n = Name(test)
        n.is_nice()
        self.assertEqual(n.nice, expected)


    def test_nice04(self):
        """
        Check if its naughty
        """
        test = 'haegwjzuvuyypxyu'
        expected = False
        n = Name(test)
        n.is_nice()
        self.assertEqual(n.nice, expected)


    def test_nice05(self):
        """
        Check if its naughty
        """
        test = 'dvszwmarrgswjxmb'
        expected = False
        n = Name(test)
        n.is_nice()
        self.assertEqual(n.nice, expected)

if __name__ == '__main__':
    unittest.main()
