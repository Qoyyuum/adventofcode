from dataclasses import dataclass

@dataclass
class Trebuchet:
    def __init__(self, puzzle_input):
        self.calibration = self.read_calibration_doc(puzzle_input)
        self.numbers = {
            "one" : '1',
            "two" : '2',
            "three" : '3',
            "four" : '4',
            "five" : '5',
            "six" : '6',
            "seven" : '7',
            "eight" : '8',
            "nine" : '9' 
        }

    def read_calibration_doc(self, doc):
        with open(doc, 'r') as file:
            return file.readlines()

    def get_first_digit(self, line):
        first_index = 0
        first_key = ''
        for i in range(len(line)):
            if line[i].isdigit():
                first_index = i
                first_key = line[i]
                break

        for key, value in self.numbers.items():
            if line.find(key) >= 0 and line.find(key) <= first_index:
                first_index = line.find(key)
                first_key = value

        if first_key == '':
            raise ValueError("First digit not found!", line)
        return first_key

    def get_last_digit(self, line):
        last_index = 0
        last_key = ''
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                last_index = i
                last_key = line[i]
                break

        for key, value in self.numbers.items():
            try:
                if line.rindex(key) >= last_index:
                    last_index = line.rindex(key)
                    last_key = value
            except ValueError:
                continue
        if last_key == '':
            raise ValueError("Last digit not found!", line)
        return last_key

    def calculate_sum(self):
        numbers = []
        for line in self.calibration:
            line = line.strip()
            first_digit = self.get_first_digit(line)
            last_digit = self.get_last_digit(line)
            #print(f"{line=} {first_digit=} {last_digit=}")
            numbers.append(int(first_digit + last_digit))
        #print(numbers)
        return sum(numbers)


if __name__ == "__main__":
    t = Trebuchet("input.txt")
    #print(f"Answer for Part 1 of Day 1: {t.calculate_sum()}") # Code has been changed to fit for Part 2 and no longer is valid for Part 1. 
    print(f"Answer for Part 2 of Day 1: {t.calculate_sum()}")
