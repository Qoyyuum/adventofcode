from dataclasses import dataclass
import re


@dataclass
class Bag:
    def __init__(self, puzzle_input):
        self.game_info = self.read_file(puzzle_input)
        self.games = []
        self.possible_games = []
        self.parse_game_info()

    def read_file(self, puzzle_input):
        with open(puzzle_input, "r") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        return lines

    def total_possible_games(self):
        return sum(self.possible_games)

    def get_max_cubes_per_color(self):
        power_cubes = []
        for game in self.games:
            # print(f"{game=}")
            power_cube = (
                (max(game.get("red")))
                * (max(game.get("blue")))
                * (max(game.get("green")))
            )
            # print(
            # f"{game.get('id')}: Red {max(game.get('red'))} , Green {max(game.get('green'))} , Blue {max(game.get('blue'))}"
            # )
            # print("Power Cube is : ", power_cube)
            power_cubes.append(power_cube)
        return sum(power_cubes)

    def get_possible_games(self, condition):
        """Go through the games list and see if it fulfills the game condition
        @param condition is a dictionary
        e.g. {'red' : 12, 'green' : 13, 'blue' : 14}"""
        # print(f"{self.games=}")
        for index in range(len(self.games)):
            # print(
            # f"{self.games[index].get('id')}: {self.games[index].get('red')=} {self.games[index].get('green')=} {self.games[index].get('blue')=}"
            # )
            if (
                max(self.games[index].get("red")) <= condition["red"]
                and max(self.games[index].get("blue")) <= condition["blue"]
                and max(self.games[index].get("green")) <= condition["green"]
            ):
                self.possible_games.append(self.games[index].get("id"))
        return self.possible_games

    def parse_game_info(self):
        """Parse through each line and extract Game ID, and number of cubes"""
        for game in self.game_info:
            id, cubes = game.split(":")
            temp = {}
            temp["id"] = self.get_game_id(id)
            temp["red"] = self.get_red_cubes(cubes)
            temp["blue"] = self.get_blue_cubes(cubes)
            temp["green"] = self.get_green_cubes(cubes)
            self.games.append(temp)
        return self.games

    def get_game_id(self, text):
        game_id_pattern = r"^Game\s+(\d+)"
        try:
            id = re.search(game_id_pattern, text)
            if id is None:
                raise AttributeError()
            return int(id.group(1))
        except AttributeError:
            raise ValueError("Game ID not found in ", text)

    def get_blue_cubes(self, text):
        blue_cube_pattern = r"(\d+)\s+blue"
        try:
            blues = re.findall(blue_cube_pattern, text)
            blues = list(map(int, blues))
            return blues
        except AttributeError:
            print("Blue cubes not found in ", text)
        return ["0"]

    def get_red_cubes(self, text):
        red_cube_pattern = r"(\d+)\s+red"
        try:
            reds = re.findall(red_cube_pattern, text)
            reds = list(map(int, reds))
            return reds
        except AttributeError:
            print("Red cubes not found in ", text)
        return ["0"]

    def get_green_cubes(self, text):
        green_cube_pattern = r"(\d+)\s+green"
        try:
            greens = re.findall(green_cube_pattern, text)
            greens = list(map(int, greens))
            return greens
        except AttributeError:
            print("Green cubes not found in ", text)
        return ["0"]


if __name__ == "__main__":
    bag = Bag("input.txt")
    condition = {"red": 12, "green": 13, "blue": 14}
    bag.get_possible_games(condition)
    print(f"Answer for Part 1 of Day 2: {bag.total_possible_games()}")
    print(f"Answer for Part 2 of Day 2: {bag.get_max_cubes_per_color()}")
