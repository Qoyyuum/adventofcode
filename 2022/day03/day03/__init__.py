from dataclasses import dataclass

@dataclass
class Compartment:
    items:str = ''
    left:str = ''
    right:str = ''
    
    def __post_init__(self):
        self.left = self.items[:int(len(self.items)/2)]
        self.right = self.items[int(len(self.items)/2):]

    def find_common_item(self):
        ... # Something to do with set

@dataclass
class Rucksack:
    compartment:Compartment


if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        data = file.read().strip()
        common_items = []
        r = Rucksack(data)
        print(r)
