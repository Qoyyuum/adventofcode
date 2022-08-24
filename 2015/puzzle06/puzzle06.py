from dataclasses import dataclass

@dataclass
class LightGrid:
    x:int
    y:int

    def __post_init__(self):
        """
        Sets up a grid of lights with default off (0)
        with size supplied in x and y
        """
        self.grid = {}
        self.lights_on = 0
        self.brightness = 0
        for x in range(self.x):
            for y in range(self.y):
                self.grid[x,y] = {"on": False, "brightness": 0}
        return self.grid

    def on(self, start, end) -> None:
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                self.grid[x, y]["on"] = True
                self.grid[x, y]["brightness"] += 1
        return

    def off(self, start, end) -> None:
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                self.grid[x, y]["on"] = False
                if self.grid[x,y]["brightness"] > 0:
                    self.grid[x, y]["brightness"] -= 1
        return

    def toggle(self, start, end) -> None:
        for x in range(int(start[0]), int(end[0])+1):
            for y in range(int(start[1]), int(end[1])+1):
                if self.grid[x,y]["on"]:
                    self.grid[x,y]["on"] = False
                else:
                    self.grid[x,y]["on"] = True
                self.grid[x,y]["brightness"] += 2
        return

    def count_lights_lit(self):
        for keys in self.grid.values():
            if keys["on"]:
                self.lights_on += 1
            self.brightness += keys["brightness"]
        return self.lights_on
                
def solve():
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
    lg.count_lights_lit()
    print(f'{lg.lights_on = }')
    print(f'{lg.brightness = }')
    return lg.lights_on, lg.brightness

if __name__ == '__main__':
    #main()
    start = 0,0
    end = 999,0
    lg = LightGrid(1000,1000)
    lg.on(start, (999,999))
    lg.toggle(start,end)
    lg.count_lights_lit()
    print(lg.lights_on)


"Ironduxe_01"
