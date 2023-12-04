from dataclasses import dataclass

@dataclass
class Trebuchet:
    def __init__(self, puzzle_input):
        self.calibration = self.read_calibration_doc(puzzle_input)

    def read_calibration_doc(self, doc):
        with open(doc, 'r') as file:
            return file.readlines()

    def calculate_sum(self):
        numbers = [list(filter(lambda c: c.isdigit(), line)) for line in self.calibration]
        numbers = list(map(lambda numlist: int(numlist[0] + numlist[-1]), numbers))
        return sum(numbers)

if __name__ == "__main__":
    t = Trebuchet("input.txt")
    print(f"Answer for Part 1 of Day 1: {t.calculate_sum()}")
