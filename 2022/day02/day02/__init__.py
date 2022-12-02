from dataclasses import dataclass

@dataclass
class RPS:
    total_score:int = 0

    def battle(self, opponent_action:str, player_action:str, part1:bool=False) -> None:
        """
        Opponent comparisons
        """
        referee = Referee()
        o = Opponent(opponent_action)
        p = Player(player_action)
        self.total_score += referee.check_pair(o,p,part1)


    def play(self, strategy_input_file:str, part1:bool=True) -> int:
        """
        Starts the game. Supply a text input file of rock paper scissors game 
        """
        with open(strategy_input_file, 'r') as file:
            strategy = file.read().splitlines()
        for strat in strategy:
            self.battle(strat[0], strat[2], part1)
        print(self.total_score)
        return self.total_score


@dataclass
class Opponent:
    action:str = ""

@dataclass
class Player:
    action:str = ""

@dataclass
class Referee:
    player_win:int = 6
    player_lost:int = 0
    player_draw:int = 3

    player_winning_pairs = {
            "A":"Y",
            "B":"Z",
            "C":"X",
            }
    player_losing_pairs = {
            "A":"Z",
            "B":"X",
            "C":"Y",
            }
    player_draw_pairs = {
            "A":"X",
            "B":"Y",
            "C":"Z",
            }


    player_action_score = {
            "X":1, #Rock
            "Y":2, #Paper
            "Z":3, #Scissors
            }

    def check_pair(self, opponent:str, player:str, part1:bool=False) -> int:
        if part1:
            if self.player_winning_pairs[opponent.action] == player.action:
                return (self.player_win + self.player_action_score[player.action])
            if self.player_losing_pairs[opponent.action] == player.action:
                return (self.player_lost + self.player_action_score[player.action])
            if self.player_draw_pairs[opponent.action] == player.action:
                return (self.player_draw + self.player_action_score[player.action])
        else:
            if player.action == 'X': # To lose
                return self.player_lost + self.player_action_score[self.player_losing_pairs[opponent.action]]
            if player.action == 'Y': # To draw
                return self.player_draw + self.player_action_score[self.player_draw_pairs[opponent.action]]
            if player.action == 'Z': # To win
                return self.player_win + self.player_action_score[self.player_winning_pairs[opponent.action]]

if __name__ == "__main__":
    game = RPS()
    game.play('input.txt', False)
