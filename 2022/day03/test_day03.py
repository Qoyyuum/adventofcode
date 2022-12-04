import unittest

from day03 import Rucksack, find_badge_between_rucksacks

class TestRucksack(unittest.TestCase):
    def setUp(self):
        with open('test_input.txt', 'r') as file:
            self.data = file.readlines()

    def test_part_1(self):
        "Total sum is 157"
        rucksacks_sums = []
        for items in self.data:
            items.strip()
            r = Rucksack(items)
            r.split()
            r.find_common_item(r.left, r.right)
            one_rucksack_sum = r.sum_common_items(r.common_items)
            rucksacks_sums.append(one_rucksack_sum)
        expected = 157
        self.assertEqual(sum(rucksacks_sums), expected)

    def test_part_2_badges(self):
        "First 3 elf group badge is r. Second 3 elf group is Z."
        badges = []
        elf_group = []
        for items in self.data:
            items.strip()
            r = Rucksack(items)
            if len(elf_group) < 3:
                elf_group.append(r)
            if len(elf_group) == 3:
                badges.append(find_badge_between_rucksacks(elf_group))
                elf_group = []
        expected = ['r', 'Z']
        self.assertEqual(badges, expected)

    def test_part_2_sum_badges(self):
        "Sum of badges r and Z is 70"
        badges = []
        elf_group = []
        for items in self.data:
            items.strip()
            r = Rucksack(items)
            if len(elf_group) < 3:
                elf_group.append(r)
            if len(elf_group) == 3:
                badges.append(find_badge_between_rucksacks(elf_group))
                elf_group = []
        result = Rucksack.sum_common_items(badges)
        expected = 70
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
