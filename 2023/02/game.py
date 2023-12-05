from dataclasses import dataclass
import re

@dataclass
class Bag:
    def __init__(self, puzzle_input):
        self.game_info = self.read_file(puzzle_input)
        self.games = {}
        self.possible_games = [] 

    def read_file(self, puzzle_input):
        with open(puzzle_input, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        return lines

    def get_possible_games(self, condition):
        """Go through the games list and see if it fulfills the game condition
        @param condition is a dictionary
        e.g. {'red' : 12, 'green' : 13, 'blue' : 14}"""
        for game in self.games:
            if game['red'] == condition['red'] and game['blue'] == condition['blue'] and game['green'] == condition['green']:
                self.possible_games.append(game['id'])
        return self.possible_games

    def parse_game_info(self):
        """Parse through each line and extract Game ID, and number of cubes"""
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        for game in self.game_info:
            self.games['id'] = self.get_game_id(game)
            self.games['red'] = self.get_red_cubes(game)
            self.games['blue'] = self.get_blue_cubes(game)
            self.games['green'] = self.get_green_cubes(game)
        return self.games


    def get_game_id(self, text):
        game_id_pattern = r'^Game\s+(\d+)'
        try:
            id = re.search(game_id_pattern, text)
            return id.group(1)
        except AttributeError:
            raise ValueError("Game ID not found in ", text)

    def get_blue_cubes(self, text):
        blue_cube_pattern = r'(\d+)\s+blue'
        try:
            blues = re.search(blue_cube_pattern, text)
        except AttributeError:
            print("Blue cubes not found in ", text)

    def get_red_cubes(self, text):
        red_cube_pattern = r'(\d+)\s+red'
        try:
            reds = re.search(red_cube_pattern, text)
            return reds.group(1)
        except AttributeError:
            print("Red cubes not found in ", text)

    def get_green_cubes(self, text):
        green_cube_pattern = r'(\d+)\s+green'
        try:
            greens = re.search(green_cube_pattern, text)
            return greens.group(1)
        except AttributeError:
            print("Green cubes not found in ", text)

if __name__ == "__main__":
    bag = Bag('test_input.txt')
    condition = {'red' : 12, 'green' : 13, 'blue' : 14}
    print(bag.get_possible_games(condition))
