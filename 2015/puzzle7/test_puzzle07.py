import unittest

from puzzle07 import LogicGate, Wire

#class TestPuzzle07(unittest.TestCase):
def test():
#def test(self):
    sample = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
    """
    left, right = sample.split(' -> ')
    print(f"{left = }")
    print(f"{right = }")


if __name__ == '__main__':
    test()
