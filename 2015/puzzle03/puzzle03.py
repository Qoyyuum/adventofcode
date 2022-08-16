from dataclasses import dataclass, field

@dataclass
class Santa:
    houses_visited:int = 1
    x:int = 0
    y:int = 0
    houses:dict[tuple, int] = field(default_factory=dict)

    def travel(self, moves):
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

    def house_check(self):
        if (self.x, self.y) in self.houses.keys():
            self.houses[(self.x, self.y)] += 1
        else:
            self.houses[(self.x, self.y)] = 1

    def count_houses(self):
        self.houses_visited = len(self.houses)

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

if __name__ == '__main__':
    s = Santa()
    #s.travel("^v^v^v")
    #s.travel(">")
    with open('input_puzzle03.txt', 'r') as f:
        movelist = f.readline()
    s.travel(movelist)
    print(s.houses_visited)
