from dataclasses import dataclass, field

@dataclass
class Santa:
    houses_visited:int = 1
    x:int = 0
    y:int = 0
    houses:dict[tuple, int] = field(default_factory=dict)

    def travel(self, moves) -> None:
        self.houses = {(0,0):1} #Init
        for m in moves:
            if m == "^":
                self.up()
            if m == "v":
                self.down()
            if m == ">":
                self.right()
            if m == "<":
                self.left()
            self.house_check()
        self.count_houses()

    def house_check(self) -> None:
        if (self.x, self.y) in self.houses.keys():
            self.houses[(self.x, self.y)] += 1
        else:
            self.houses[(self.x, self.y)] = 1
    
    def count_houses(self) -> None:
        self.houses_visited = len(self.houses)

    def up(self) -> None:
        self.y += 1

    def down(self) -> None:
        self.y -= 1

    def left(self) -> None:
        self.x -= 1

    def right(self) -> None:
        self.x += 1

def santa_and_robo_santa_combo(m) -> int:
    """
    Split the moves between Santa and Robo-Santa.
    This is for Part Two.

    @param moves = A string or a list of movements ^v<>
    @result = integer
    """
    santa = Santa()
    robosanta = Santa()
    santaMoves = []
    robosantaMoves = []
    for i,v in enumerate(m):
        if i % 2 == 0:
            santaMoves.append(v)
        else:
            robosantaMoves.append(v)
    santa.travel(santaMoves)
    robosanta.travel(robosantaMoves)
    merged_houses = santa.houses | robosanta.houses
    return len(merged_houses)

if __name__ == '__main__':
    s = Santa()
    s.travel("^v^v^v")
    s.travel(">")
    with open('input_puzzle03.txt', 'r') as f:
        movelist = f.readline()
    s.travel(movelist)
    print("For Part One")
    print(s.houses_visited)
    print("For Part Two")
    print(santa_and_robo_santa_combo(movelist))
