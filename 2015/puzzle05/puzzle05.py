from dataclasses import dataclass

@dataclass
class Name:
    text:str

    def check_vowels(self) -> int:
        vowels = 'aeiou'
        self.vowels = 0
        for t in self.text:
            if t in vowels:
                self.vowels += 1
        return self.vowels

    def check_repeatable_letter(self, gap:int = 0) -> bool:
        self.repeatedletter = False
        gap += 1 
        #print(f"{gap=}")
        try:
            for index, letter in enumerate(self.text):
                #print(f'{letter} == {self.text[index+gap]} = {letter == self.text[index+gap]}')
                if letter == self.text[index+gap]:
                    self.repeatedletter = True
                    break
        except IndexError:
            pass
        return self.repeatedletter

    def check_forbidden_strings(self) -> bool:
        self.forbidden = False
        forbidden = ['ab', 'cd', 'pq', 'xy']
        for f in forbidden:
            if f in self.text:
                self.forbidden = True
                break
        return self.forbidden

    def is_nice(self, checks:int=1) -> bool:
        """checks == 1 for Part One as check the list once. checks == 2 for Part Two as check the list twice"""
        self.nice = False
        if checks==1:
            if self.check_forbidden_strings() == False and (self.check_vowels() >= 3 and self.check_repeatable_letter()):
                self.nice = True
        if checks==2:
            if self.check_repeatable_letter(1) and self.check_non_overlapping_letter_pairs():
                self.nice = True
        return self.nice

    def check_non_overlapping_letter_pairs(self) -> bool:
        self.none_overlapped = False
        for i in range(len(self.text)-1):
            if self.text.count(f'{self.text[i]}{self.text[i+1]}') > 1:
                self.none_overlapped = True
                break
        return self.none_overlapped

def main():
    puzzle = 'input_puzzle05.txt'
    total_nice = 0
    total_nice_twice = 0
    with open(puzzle, 'r') as f:
        lines = f.readlines()
    for line in lines:
        n = Name(line)
        if n.is_nice(): total_nice += 1
        if n.is_nice(2): total_nice_twice += 1
    print(f"{total_nice = } out of {len(lines)}")
    print(f"{total_nice_twice = } out of {len(lines)}")

if __name__ == '__main__':
    main()
