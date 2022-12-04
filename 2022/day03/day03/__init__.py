from dataclasses import dataclass, field
from string import ascii_letters
from typing import List

@dataclass
class Rucksack:
    items:str
    left:str = ''
    right:str = ''
    common_items:List[str] = field(default_factory=list)

    def split(self) -> None:
        """Split exactly half of the length of the items into left and right"""
        self.left = self.items[:int(len(self.items)/2)]
        self.right = self.items[int(len(self.items)/2):]

    def find_common_item(self, left:str, right:str) -> List:
        """Find the common items between left and right after split() and return them."""
        temp_items = []
        for item in left:
            if item in right:
                temp_items.append(item)
        self.common_items = set(temp_items)
        return self.common_items

    @staticmethod
    def sum_common_items(common_items:List[str]) -> int:
        """Sum the items based on priority of ascii letters"""
        priority = {}
        for index, letter in enumerate(ascii_letters):
            priority[letter] = index+1
        rucksack_sum = 0
        for item in common_items:
            rucksack_sum += priority.get(item)
        return rucksack_sum

def find_badge_between_rucksacks(list_of_three_rucksacks:List[str]) -> str:
    """Find the common badge between Rucksack objects"""
    first_rucksack, second_rucksack, third_rucksack = list_of_three_rucksacks
    #print(f'Rucksacks:\nFirst = {first_rucksack.items}\nSecond = {second_rucksack.items}\nThird = {third_rucksack.items}')
    for item_list_one in first_rucksack.items:
        for item_list_two in second_rucksack.items:
            for item_list_three in third_rucksack.items:
                if item_list_one == item_list_two == item_list_three:
                    return item_list_one



if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = file.readlines()
        rucksacks_sums = []
        badges = []
        elf_group = []
        for items in data:
            items.strip()
            r = Rucksack(items)
            if len(elf_group) < 3:
                elf_group.append(r)
            if len(elf_group) == 3:
                badges.append(find_badge_between_rucksacks(elf_group))
                elf_group = []
            r.split()
            r.find_common_item(r.left, r.right)
            one_rucksack_sum = Rucksack.sum_common_items(r.common_items)
            rucksacks_sums.append(one_rucksack_sum)
        answer_for_part1 = sum(rucksacks_sums)
        answer_for_part2 = Rucksack.sum_common_items(badges)
        print(f'Part 1: {answer_for_part1}')
        print(f'Part 2: {answer_for_part2}')
