from dataclasses import dataclass

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

def solve01(input_file:str) -> int:
    """Find the Elf carrying the most calories. How many total calories is that Elf carrying?"""
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

    # Find the Elf carrying the most calories
    elves.sort()
    most_calories = elves[-1]
    print(f'Answer to Part 1:\n{most_calories.calories}')
    top3 = elves[-3:]
    total_top3_calories = 0
    for e in top3:
        total_top3_calories += e.calories
    print(f'Answer to Part 2:\n{total_top3_calories}')

if __name__ == "__main__":
    solve01("input.txt")
