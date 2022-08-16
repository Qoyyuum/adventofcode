import unittest

from puzzle03 import Santa, santa_and_robo_santa_combo

class TestPuzzle03(unittest.TestCase):

    def test01(self):
        """
        Test to see if it returns 2 houses delivered by going in
        only one direction.
        
        @result = integer
        """
        moves = ">"
        actual_houses = 2
        santa = Santa()
        santa.travel(moves)
        self.assertEqual(santa.houses_visited, actual_houses)

    def test02(self):
        """
        Test to see if it returns 4 houses delivered by going in
        only a square box direction.
        
        @result = integer
        """
        moves = "^>v<"
        actual_houses = 4
        santa = Santa()
        santa.travel(moves)
        self.assertEqual(santa.houses_visited, actual_houses)

    def test03(self):
        """
        Test to see if it returns 2 houses delivered by going in
        only a up and down direction.
        
        @result = integer
        """
        moves = "^v^v^v^v^v"
        actual_houses = 2
        santa = Santa()
        santa.travel(moves)
        self.assertEqual(santa.houses_visited, actual_houses)

    def test04(self):
        """
        Test for Santa and RoboSanta to deliver 3 houses

        @result = integer
        """
        moves = "^>v<"
        combined_houses = santa_and_robo_santa_combo(moves)
        actual_houses = 3
        self.assertEqual(combined_houses, actual_houses)

    def test05(self):
        """
        Test for Santa and RoboSanta to deliver 3 houses

        @result = integer
        """
        moves = "^>v<"
        combined_houses = santa_and_robo_santa_combo(moves)
        actual_houses = 3
        self.assertEqual(combined_houses, actual_houses)

    def test06(self):
        """
        Test for Santa and RoboSanta to deliver 3 houses

        @result = integer
        """
        moves = "^v^v^v^v^v"
        combined_houses = santa_and_robo_santa_combo(moves)
        actual_houses = 11
        self.assertEqual(combined_houses, actual_houses)


if __name__ == '__main__':
    unittest.main()
