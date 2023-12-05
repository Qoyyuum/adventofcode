from string import punctuation


class Engine:
    def __init__(self, engine_schematic):
        self.schematic = self.read_file(engine_schematic)
        self.symbols = "".join(punctuation.split("."))

    def read_file(self, file):
        with open(file, "r") as f:
            return [line.strip() for line in f.readlines()]

    def find_symbol(self):
        for no, line in enumerate(self.schematic):
            for s in self.symbols:
                if s in line:
                    symbol_x_position = line.find(s)
                    symbol_y_position = no
                    symbol_position = (symbol_x_position, symbol_y_position)
                    self.find_nearest_number(symbol_position)
                else:
                    continue

    def find_nearest_number(self, center_position):
        """Check around the center position (x,y coordinates) for numbers"""
        x = center_position[0]
        y = center_position[1]
        # center = self.schematic[x][y]
        check_left = self.schematic[x][y - 1]
        check_top_left = self.schematic[x - 1][y - 1]
        check_top = self.schematic[x - 1][y]
        check_top_right = self.schematic[x - 1][y + 1]
        check_right = self.schematic[x][y + 1]
        check_bottom_right = self.schematic[x + 1][y + 1]
        check_bottom = self.schematic[x + 1][y]
        check_bottom_left = self.schematic[x + 1][y - 1]
        numbers = []
        if check_left.isdigit():
            numbers.append(self.check_whole_number((x, y - 1)))
        if check_right.isdigit():
            numbers.append(self.check_whole_number((x, y + 1)))

        # Check tops
        if (
            check_top_left.isdigit()
            and check_top.isdigit()
            and check_top_right.isdigit()
        ):
            numbers.append(self.check_whole_number((x - 1, y)))
        elif check_top_left.isdigit():
            numbers.append(self.check_whole_number((x - 1, y - 1)))
        if check_top_right.isdigit():
            numbers.append(self.check_whole_number((x - 1, y + 1)))
        elif check_top.isdigit():
            numbers.append(self.check_whole_number((x - 1, y)))

        # Check bottoms
        if (
            check_bottom_right.isdigit()
            and check_bottom.isdigit()
            and check_bottom_left.isdigit()
        ):
            numbers.append(self.check_whole_number((x + 1, y)))
        elif check_bottom_right.isdigit():
            numbers.append(self.check_whole_number((x + 1, y + 1)))
        if check_bottom_left.isdigit():
            self.check_whole_number((x + 1, y - 1))

    def check_whole_number(self, detected_position):
        """Checks and finds the whole number left and right of the detected position"""
        first_y_index = detected_position[1]
        last_y_index = detected_position[1]
        row = detected_position[0]
        if detected_position[1] > 0:
            for y in range(detected_position[1], -1, -1):
                if (
                    self.schematic[row][y] == "."
                    or self.schematic[row][y] in self.symbols
                    or y == 0
                ):  # check left of it for extra digits
                    first_y_index = y
                    break
        if detected_position[1] < len(self.schematic[row]):
            for y in range(detected_position[1]):
                if (
                    self.schematic[row][y] == "."
                    or self.schematic[row][y] in self.symbols
                    or y == len(self.schematic[row]) - 1
                ):  # check right of it for extra digits
                    last_y_index = y
                    break
        return self.schematic[row][first_y_index:last_y_index]


if __name__ == "__main__":
    e = Engine("test_input.txt")
