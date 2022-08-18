import unittest

from puzzle05 import Name

class TestPuzzle05(unittest.TestCase):
    @unittest.skip("For Part Two")
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


    @unittest.skip("For Part Two")
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

    @unittest.skip("For Part Two")
    def test_three_vowels03(self):
        """
        It has at least 3 vowels

        @result > 3
        """
        test = 'aeiouaeiouaeiou'
        expected = 15
        n = Name(test)
        n.check_vowels()
        self.assertEqual(n.vowels, expected)

    @unittest.skip("For Part Two")
    def test_repeatable_letter01(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'xx'
        n = Name(test)
        n.check_repeatable_letter()
        self.assertTrue(n.repeatedletter)

    @unittest.skip("For Part Two")
    def test_repeatable_letter02(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'abcdde'
        n = Name(test)
        n.check_repeatable_letter()
        self.assertTrue(n.repeatedletter)

    @unittest.skip("For Part Two")
    def test_repeatable_letter03(self):
        """
        Contains at least 1 repeatable letter

        @result = bool
        """
        test = 'aabbccdd'
        n = Name(test)
        n.check_repeatable_letter()
        self.assertTrue(n.repeatedletter)
    
    @unittest.skip("For Part Two")
    def test_forbidden_strings01(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'ab'
        n = Name(test)
        n.check_forbidden_strings()
        self.assertTrue(n.forbidden)
    
    @unittest.skip("For Part Two")
    def test_forbidden_strings02(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'cd'
        n = Name(test)
        n.check_forbidden_strings()
        self.assertTrue(n.forbidden)
    
    @unittest.skip("For Part Two")
    def test_forbidden_strings03(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'pq'
        expected = True
        n = Name(test)
        n.check_forbidden_strings()
        self.assertTrue(n.forbidden)

    @unittest.skip("For Part Two")
    def test_forbidden_strings04(self):
        """
        Should not contain 'ab'

        @result = bool
        """
        test = 'xy'
        n = Name(test)
        n.check_forbidden_strings()
        self.assertTrue(n.forbidden)

    @unittest.skip("For Part Two")
    def test_nice01(self):
        """
        Check if its nice
        """
        test = 'ugknbfddgicrmopn'
        n = Name(test)
        n.is_nice()
        self.assertTrue(n.nice)

    @unittest.skip("For Part Two")
    def test_nice02(self):
        """
        Check if its nice
        """
        test = 'aaa'
        n = Name(test)
        n.is_nice()
        self.assertTrue(n.nice)


    @unittest.skip("For Part Two")
    def test_nice03(self):
        """
        Check if its naughty
        """
        test = 'jchzalrnumimnmhp'
        n = Name(test)
        n.is_nice()
        self.assertFalse(n.nice)


    @unittest.skip("For Part Two")
    def test_nice04(self):
        """
        Check if its naughty
        """
        test = 'haegwjzuvuyypxyu'
        n = Name(test)
        n.is_nice()
        self.assertFalse(n.nice)


    @unittest.skip("For Part Two")
    def test_nice05(self):
        """
        Check if its naughty
        """
        test = 'dvszwmarrgswjxmb'
        n = Name(test)
        n.is_nice()
        self.assertFalse(n.nice)

    def test_pair_of_letters01(self):
        """
        Check if it has a pair of non overlapping letters
        """
        test = 'xyxy'
        n = Name(test)
        n.check_non_overlapping_letter_pairs()
        self.assertTrue(n.none_overlapped)

    def test_pair_of_letters02(self):
        """
        Check if it has a pair of non overlapping letters
        """
        test = 'aabcdefgaa'
        n = Name(test)
        n.check_non_overlapping_letter_pairs()
        self.assertTrue(n.none_overlapped)

    def test_pair_of_letters03(self):
        """
        Check if it doesn't has a pair of non overlapping letters
        """
        test = 'aaa'
        n = Name(test)
        n.check_non_overlapping_letter_pairs()
        self.assertFalse(n.none_overlapped)

    def test_repeatable_letter_with_one_letter_gap01(self):
        """
        Check if xyx has a repeatable letter with one letter in between.
        """
        test = 'xyx'
        n = Name(test)
        n.check_repeatable_letter(1)
        self.assertTrue(n.repeatedletter)

    def test_repeatable_letter_with_one_letter_gap02(self):
        """
        Check if abcdefeghi has a repeatable letter with one letter in between.
        """
        test = 'abcdefeghi'
        n = Name(test)
        n.check_repeatable_letter(1)
        self.assertTrue(n.repeatedletter)

    def test_repeatable_letter_with_one_letter_gap03(self):
        """
        Check if aaa has a repeatable letter with one letter in between.
        """
        test = 'aaa'
        n = Name(test)
        n.check_repeatable_letter(1)
        self.assertTrue(n.repeatedletter)

    def test_nice_twice01(self):
        """
        Check if qjhvhtzxzqqjkmpb nice for part 2
        """
        test = 'qjhvhtzxzqqjkmpb'
        n = Name(test)
        n.is_nice_twice()
        self.assertTrue(n.nice)

    def test_nice_twice02(self):
        """
        Check if xxyxx nice for part 2
        """
        test = 'xxyxx'
        n = Name(test)
        n.is_nice_twice()
        self.assertTrue(n.nice)

    def test_nice_twice03(self):
        """
        Check if uurcxstgmygtbstg naughty for part 2
        """
        test = 'uurcxstgmygtbstg'
        n = Name(test)
        n.is_nice_twice()
        self.assertFalse(n.nice)

    def test_nice_twice04(self):
        """
        Check if ieodomkazucvgmuy naughty for part 2
        """
        test = 'ieodomkazucvgmuy'
        n = Name(test)
        n.is_nice_twice()
        self.assertFalse(n.nice)

if __name__ == '__main__':
    unittest.main()
