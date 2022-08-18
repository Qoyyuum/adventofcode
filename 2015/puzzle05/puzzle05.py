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
        if gap != 0 and gap > 0:
            gap += 1 # Lists are zero indexed
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
        return self.forbidden

    def is_nice(self) -> bool:
        self.nice = False
        if self.check_forbidden_strings() == False and (self.check_vowels() >= 3 and self.check_repeatable_letter()):
            self.nice = True
        return self.nice

    def check_non_overlapping_letter_pairs(self) -> bool:
        self.none_overlapped = False
        pairs = list(enumerate([self.text[i:i+2] for i in range(len(self.text) - 1)]))
        #print(f"{pairs=}")
        pairs = [(b, a) for a, b in pairs]
        #print(f"{pairs=}")
        pairs.sort()
        #print(pairs)
        d = {k:v for k,v in  pairs}
        print(d)
        return self.none_overlapped

    def is_nice_twice(self) -> bool:
        self.nice = False
        #print(f"{self.text = } has {self.check_repeatable_letter(1) = } and {self.check_non_overlapping_letter_pairs() = }, so its {self.check_repeatable_letter(1) == self.check_non_overlapping_letter_pairs()}")
        if self.check_repeatable_letter(1) and self.check_non_overlapping_letter_pairs():
            self.nice = True
        return self.nice

if __name__ == '__main__':
    puzzle = 'input_puzzle05.txt'
    total_nice = 0
    #with open(puzzle, 'r') as f:
    #    lines = f.readlines()
    #for line in lines:
    #    n = Name(line)
    #    if n.is_nice(): total_nice += 1
    #print(f"{total_nice = } out of {len(lines)}")
    n = Name('aabcdefgaa')
    n.check_non_overlapping_letter_pairs()
    #n.is_nice_twice()
    print(n.none_overlapped)
