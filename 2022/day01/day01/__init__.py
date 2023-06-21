from dataclasses import dataclass
from typing import List

@dataclass
class Elf:
    calories:int = 0

    def add(self, food:int) -> int:
        """Sum the food calories of this Elf"""
        self.calories += food

    def __lt__(self, other) -> bool:
        return self.calories < other.calories

    def __gt__(self, other) -> bool:
        return self.calories > other.calories

def Elves(input_file: str) -> List[Elf]:
    with open(input_file, 'r') as file:
        data = file.read().splitlines()

    elves = []
    elf = Elf()
    for food_item in data:
        if len(food_item) > 0:
            elf.add(int(food_item))
        else:
            elves.append(elf)
            elf = Elf()
    elves.append(elf)
    return elves

def solve01(input_file:str) -> int:
    """Find the Elf carrying the most calories. How many total calories is that Elf carrying?"""
    elves = Elves(input_file)
    elves.sort()
    most_calories = elves[-1]
    print("Find the Elf carrying the most calories. How many total calories is that Elf carrying?")
    print(f'Answer to Part 1:\n{most_calories.calories}')
    return most_calories

def solve02(input_file:str) -> int:
    """Find the top 3 Elves carrying the most calories. How many calories are those Elves carrying in total?"""
    elves = Elves(input_file)
    elves.sort()
    top3 = elves[-3:]
    total_top3_calories = 0
    for e in top3:
        total_top3_calories += e.calories
    print("Find the top 3 Elves carrying the most calories. How many calories are those Elves carrying in total?")
    print(f'Answer to Part 2:\n{total_top3_calories}')
    return total_top3_calories

if __name__ == "__main__":
    solve01("input.txt")
    solve02("input.txt")
