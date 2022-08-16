from dataclasses import dataclass

@dataclass
class Puzzle02:
    l:int
    w:int
    h:int

    def calculate_total_square_feet(self):
        side1 = (self.l)*(self.w)
        side2 = (self.w)*(self.h)
        side3 = (self.h)*(self.l)
        self.extra_paper = min([side1, side2, side3])
        self.wrapping_paper = 2*side1 + 2*side2 + 2*side3
        self.total_square_feet = self.wrapping_paper + self.extra_paper
        return self.total_square_feet

    def calculate_total_ribbon_length(self):
        sizes_sorted = [self.l, self.w, self.h]
        sizes_sorted.sort()
        self.wrapping_ribbon = sizes_sorted[0] + sizes_sorted[0] + sizes_sorted[1] + sizes_sorted[1]
        self.bow_ribbon = self.l * self.w * self.h
        return self.wrapping_ribbon + self.bow_ribbon


if __name__ == '__main__':
    data = 'input_puzzle02.txt'
    grand_total_paper = 0
    grand_total_ribbon = 0
    with open(data, 'r') as f:
        for line in f.readlines():
            l, w, h = [int(x) for x in line.split('x')]
            #print(f"{l=} {w=} {h=}")
            p = Puzzle02(l, w, h)
            total_paper = p.calculate_total_square_feet()
            #print(f"{p = }\n{total = }")
            grand_total_paper = grand_total_paper + total_paper
            total_ribbon = p.calculate_total_ribbon_length()
            grand_total_ribbon = grand_total_ribbon + total_ribbon
            
    print(f"{grand_total_paper = }")
    print(f"{grand_total_ribbon = }")
