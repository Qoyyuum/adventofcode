from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Section:
    pair:str = ''
    fully_contained:str = ''

    def split(self) -> Tuple[int, int, int, int]:
        """Call this function to split the Section.pair into 2 assignments"""
        self.pair = self.pair.strip()
        self.left, self.right = self.pair.split(',')

        left_start, left_end = self.left.split('-')
        right_start, right_end = self.right.split('-')
        left_start = int(left_start)
        left_end = int(left_end)
        right_start = int(right_start)
        right_end = int(right_end)
        return left_start, left_end, right_start, right_end

    def check_fully_contained(self) -> None:
        """Works after the Section.pair is split first and then checks which pair fully contains which or neither."""
        left_start, left_end, right_start, right_end = self.split()

        #print(f"{self.left} vs {self.right}:")
        single_digit_left = self._check_for_single_digits(left_start, left_end)
        single_digit_right = self._check_for_single_digits(right_start, right_end)

        if single_digit_left is not None:
            if right_start <= single_digit_left <= right_end:
                self.fully_contained = self.right
                #print(f"Single Digit Left fully contained! {self.fully_contained}")
                return self.fully_contained
        if single_digit_right is not None:
            if left_start <= single_digit_right <= left_end:
                self.fully_contained = self.left
                #print(f"Single Digit Right fully contained! {self.fully_contained}")
                return self.fully_contained

        # Checks if Left Start will contain Right
        if left_start <= right_start:
            if right_end <= left_end:
                self.fully_contained = self.left
                #print(f"Left fully contains Right: {self.fully_contained}")
                return self.fully_contained
        # Checks if Right Start will contain Left
        if right_start <= left_start:
            if left_end <= right_end:
                self.fully_contained = self.right
                #print(f"Right fully contains Left: {self.fully_contained}")
                return self.fully_contained
        #print("NOT fully contained")

    def _check_for_single_digits(self, start:int, end:int) -> int:
        if start == end:
            return start

    def is_overlapped(self) -> bool:
        left_start, left_end, right_start, right_end = self.split()
        if left_start <= right_start <= left_end:
            return True
        if left_start <= right_end <= left_end:
            return True
        if right_start <= left_start <= right_end:
            return True
        if right_start <= left_end <= right_end:
            return True
        return False

    @staticmethod
    def expand_int_range(start:int, end:int) -> List:
        result = []
        difference = end - start
        if difference == 0:
            return [start]
        if difference > 0:
            for d in range(difference+1):
                result.append(d+1)
        return result
        if difference < 0:
            raise ValueError()

def answer_for_part_1(input_file:str) -> int:
    fully_contained_pairs_list = []
    with open(input_file, 'r') as file:
        data = file.readlines()

    for pair in data:
        section = Section(pair)
        section.split()
        section.check_fully_contained()
        if section.fully_contained:
            fully_contained_pairs_list.append(section.fully_contained)
    print(len(fully_contained_pairs_list))
    return len(fully_contained_pairs_list)

def answer_for_part_2(input_file:str) -> int:
    fully_contained_pairs_list = []
    with open(input_file, 'r') as file:
        data = file.readlines()

    count = 0
    for pair in data:
        section = Section(pair)
        section.split()
        if section.is_overlapped():
            count += 1
    return count

if __name__ == "__main__":
    answer_for_part_1('input.txt')
