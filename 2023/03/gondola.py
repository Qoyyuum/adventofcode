from string import punctuation
import re


class Engine:
    def __init__(self, engine_schematic):
        self.schematic = self.read_file(engine_schematic)
        self.symbols = "".join(punctuation.split("."))
        self.part_numbers = []
        self.found_symbols = []

    def read_file(self, file):
        with open(file, "r") as f:
            return [line.strip() for line in f.readlines()]

    def find_symbol(self):
        for lineno, line in enumerate(self.schematic):
            for symbol in self.symbols:
                if symbol in line:
                    symbol_x_position = line.find(symbol)
                    symbol_y_position = lineno
                    symbol_position = (symbol_x_position, symbol_y_position)
                    self.found_symbols.append(symbol_position)
        return self.found_symbols

    def find_part_numbers(self):
        for symbol_position in self.found_symbols:
            found_digit_positions = self.check_surrounding_symbol(symbol_position)
            if found_digit_positions or len(found_digit_positions) > 0:
                for digit_position in found_digit_positions:
                    self.part_numbers.append(
                        self.get_the_rest_of_the_part_number(digit_position)
                    )
        return self.part_numbers

    def get_the_rest_of_the_part_number(self, found_digit_position):
        row = found_digit_position[0]
        index = found_digit_position[1]
        startindex = 0
        endindex = len(self.schematic[row]) - 1
        if index > startindex:
            for left_index in range(index, -1, -1):
                if self.schematic[row][left_index].isdigit():
                    startindex = left_index
                else:
                    break
        if index < endindex:
            for right_index in range(index, len(self.schematic[row]) + 1):
                if self.schematic[row][right_index].isdigit():
                    endindex = right_index
                else:
                    break
        return int(self.schematic[row][startindex:endindex])

    def find_partnumbers(self):
        """Find and return valid part numbers adjacent to symbols"""
        pattern = r"\b\d+\b"
        for lineno, line in enumerate(self.schematic):
            numbers = re.findall(pattern, line)
            for number in numbers:
                # print(
                # f"{number=} {line.find(number)=}"
                # )  # This would get the first occurence of that number
                startindex = line.find(number)
                endindex = startindex + len(number)
                # print(f"{startindex= } {endindex= }")
                # print(f"{self.schematic[lineno][startindex:endindex]=}")
                for y in range(startindex, endindex):
                    coordinates = (lineno, y)
                    if self.check_surrounding_element(coordinates):
                        # print("Valid part number", number)
                        self.part_numbers.append(int(number))
                        self.part_numbers = sorted(list(set(self.part_numbers)))

        return set(self.part_numbers)

    def check_surrounding_element(self, center_position):
        """position is startindex and endindex"""
        x = center_position[0]
        y = center_position[1]
        check_bottom_right, check_bottom_left, check_bottom = False, False, False
        check_left, check_right = False, False
        check_top_right, check_top_left, check_top = False, False, False
        check_left = self.schematic[x][y - 1] in self.symbols
        check_top_left = self.schematic[x - 1][y - 1] in self.symbols
        check_top = self.schematic[x - 1][y] in self.symbols
        if y < len(self.schematic[x]) - 1:
            check_right = self.schematic[x][y + 1] in self.symbols
            check_top_right = self.schematic[x - 1][y + 1] in self.symbols
        if x < len(self.schematic) - 1:
            check_bottom = self.schematic[x + 1][y] in self.symbols
            check_bottom_left = self.schematic[x + 1][y - 1] in self.symbols
        if x < len(self.schematic) - 1 and y < len(self.schematic[x]) - 1:
            check_bottom_right = self.schematic[x + 1][y + 1] in self.symbols
        if any(
            [
                check_left,
                check_top_left,
                check_top,
                check_top_right,
                check_right,
                check_bottom_left,
                check_bottom,
                check_bottom_right,
            ]
        ):
            return True
        return False

    def check_surrounding_symbol(self, center_position):
        """center_position is startindex and endindex. Check surrounding symbol if it is a digit."""
        x = center_position[0]
        y = center_position[1]
        left = x, y - 1
        top_left = x - 1, y - 1
        top = x - 1, y
        bottom = x + 1, y
        bottom_left = x + 1, y - 1
        found_digits = []
        if self.check_digit(left):
            found_digits.append(left)
        if self.check_digit(top_left):
            found_digits.append(top_left)
        if self.check_digit(top):
            found_digits.append(top)
        if y < len(self.schematic[x]) - 1:
            top_right = x - 1, y + 1
            right = x, y + 1
            if self.check_digit(top_right):
                found_digits.append(top_right)
            if self.check_digit(right):
                found_digits.append(right)
        if x < len(self.schematic) - 1:
            if self.check_digit(bottom_left):
                found_digits.append(bottom_left)
            if self.check_digit(bottom):
                found_digits.append(bottom)
        if x < len(self.schematic) - 1 and y < len(self.schematic[x]) - 1:
            bottom_right = x + 1, y + 1
            if self.schematic[bottom_right[0]][bottom_right[1]].isdigit():
                found_digits.append(bottom_right)
        return found_digits

    def check_digit(self, coordinates):
        if self.schematic[coordinates[0]][coordinates[1]].isdigit():
            return True
        return False


if __name__ == "__main__":
    e = Engine("input.txt")
    e.find_part_numbers()
    print(sum(e.part_numbers))
