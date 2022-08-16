class Puzzle01:
    def __init__(self, data):
        self.t = data
        self.floor = 0
        self.basement_position = 0

    def count_brackets(self):
        for position, f in enumerate(self.t):
            if "(" in f:
                self.floor = self.floor + 1
            if ")" in f:
                self.floor = self.floor - 1
                if self.floor <= -1:
                    self.basement_position = position + 1
        return self.floor

if __name__ == '__main__':
    data = 'input_puzzle01.txt'
    with open(data, 'r') as f:
        code = f.readline()
    p = Puzzle01(code)
    p.count_brackets()
    print(f'{p.floor = }\n{p.basement_position = }\n')


