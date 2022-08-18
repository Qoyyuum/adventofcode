from dataclasses import dataclass

@dataclass
class Name:
    text:str

    def check_vowels(self):
        vowels = 'aeiou'
        self.vowels = 0
        for t in self.text:
            if t in vowels:
                self.vowels += 1
        return self.vowels

    def check_repeatable_letter(self):
        self.repeatedletter = False
        current_letter = ''
        for t in self.text:
            if current_letter == t:
                self.repeatedletter = True
                break
            else:
                current_letter = t
        return self.repeatedletter

    def check_forbidden_strings(self):
        self.forbidden = False
        forbidden = ['ab', 'cd', 'pq', 'xy']
        for f in forbidden:
            if f in self.text:
                self.forbidden = True
        return self.forbidden

    def is_nice(self):
        self.nice = False
        if self.check_forbidden_strings() == False and (self.check_vowels() >= 3 and self.check_repeatable_letter()):
            self.nice = True
        return self.nice


if __name__ == '__main__':
    puzzle = 'input_puzzle05.txt'
    total_nice = 0
    with open(puzzle, 'r') as f:
        lines = f.readlines()
    for line in lines:
        n = Name(line)
        if n.is_nice(): total_nice += 1
    print(f"{total_nice = } out of {len(lines)}")
