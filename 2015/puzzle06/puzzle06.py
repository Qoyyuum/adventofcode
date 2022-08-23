from dataclasses import dataclass

@dataclass
class LightGrid:
    x:int
    y:int

    def __post_init__(self):
        """
        Sets up a grid of lights with default off
        with size supplied in x and y
        """
        self.grid = {}
        self.lights_on = 0
        self.lights_off = 0
        for x in range(self.x):
            for y in range(self.y):
                self.grid[x,y] = False
        self.count_lights_lit()
        return self.grid

    def on(self, start, end):
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                self.grid[x, y] = True
        return self.count_lights_lit()

    def off(self, start, end):
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                self.grid[x, y] = False
        return self.count_lights_lit()

    def toggle(self, start, end):
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                if self.grid[x,y]:
                    self.grid[x,y] = False
                else:
                    self.grid[x,y] = True
        return self.count_lights_lit()

    def count_lights_lit(self):
        from collections import Counter
        lights = Counter(self.grid.values())
        if True in lights:
            self.lights_on = lights[True]
        if False in lights:
            self.lights_off = lights[False]
        return self.lights_on
                
def main():
    lg = LightGrid(1000,1000)
    with open('input_puzzle06.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        splitLine = line.split()
        index = 1 if len(splitLine) > 4 else 0
        start = tuple(splitLine[1 + index].split(','))
        end = tuple(splitLine[3 + index].split(','))
        if splitLine[1] == 'on':
            lg.on(start,end)
        if splitLine[1] == 'off':
            lg.off(start,end)
        if splitLine[0] == 'toggle':
            lg.toggle(start,end)
    print(f'{lg.lights_on = }')

if __name__ == '__main__':
    main()
