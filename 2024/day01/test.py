from solution import mylists
import unittest


class TestDay01(unittest.TestCase):
    def test_mylists(self):
        self._extracted_from_test_mylists_6_2(
            "The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.",
            2,
            1,
            3,
        )

    def test_mylists_2(self):
        self._extracted_from_test_mylists_6_2(
            "The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.",
            1,
            2,
            3,
        )
    
    def test_mylists_3(self):
        self._extracted_from_test_mylists_6_2(
            "The third-smallest number in both lists is 3, so the distance between them is 0.",
            0,
            3,
            3,
        )

    def test_mylists_4(self):
        self._extracted_from_test_mylists_6_2(
            "The next numbers to pair up are 3 and 4, a distance of 1.", 1, 3, 4
        )

    def test_mylists_5(self):
        self._extracted_from_test_mylists_6_2(
            "The fifth-smallest numbers in each list are 3 and 5, a distance of 2.",
            2,
            3,
            5,
        )

    def test_mylists_6(self):
        self._extracted_from_test_mylists_6_2(
            "Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.",
            5,
            4,
            9,
        )

    # TODO Rename this here and in `test_mylists`, `test_mylists_2`, `test_mylists_3`, `test_mylists_4`, `test_mylists_5` and `test_mylists_6`
    def _extracted_from_test_mylists_6_2(self, arg0, arg1, arg2, arg3):
        arg0
        actual_distance = arg1
        test_distance = mylists.difference(arg2, arg3)
        self.assertEqual(actual_distance, test_distance)

        
    def test_total_distance(self):
        "The total distance between the two lists is 11."
        actual_total_distance = 11
        left_list = [1,2,3,3,3,4]
        right_list = [3,3,3,4,5,9]
        test_total_distance = mylists.total_distance(left_list, right_list)
        self.assertEqual(actual_total_distance, test_total_distance)
        
    def test_similarity1(self):
        "The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9."
        actual_similarity = 9
        left_number = 3
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)
    
    def test_similarity2(self):
        "The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4."
        actual_similarity = 4
        left_number = 4
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)
    
    def test_similarity3(self):
        "The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase."
        actual_similarity = 0
        left_number = 2
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)
        
    def test_similarity4(self):
        "The fourth number, 1, also does not appear in the right list."
        actual_similarity = 0
        left_number = 1
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)
        
    def test_similarity5(self):
        "The fifth number, 3, appears in the right list three times; the similarity score increases by 9."
        actual_similarity = 9
        left_number = 3
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)

        
    def test_similarity6(self):
        "The last number, 3, appears in the right list three times; the similarity score again increases by 9."
        actual_similarity = 9
        left_number = 3
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.similarity(left_number, right_list)
        self.assertEqual(actual_similarity, test_similarity)
    
    def test_final_similarity_score(self):
        "For these examples lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9)."
        actual_similarity = 31
        left_list = [1,2,3,3,3,4]
        right_list = [3,3,3,4,5,9]
        test_similarity = mylists.total_similarity(left_list, right_list)
        self.assertEqual(actual_similarity, test_similarity)