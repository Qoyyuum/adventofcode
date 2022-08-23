import unittest

from puzzle06 import LightGrid

class TestPuzzle06(unittest.TestCase):

    def test_turn_on_all_lights(self):
        """
        Turn on all lights from 0,0 through 999,999
        """
        start = 0,0
        end = 999,999
        expected = 1_000_000
        lg = LightGrid(1000,1000)
        lg.on(start, end)
        self.assertEqual(lg.lights_on, expected)
        
    def test_toggle_lights01(self):
        """
        Toggle lights from 0,0 through 999,0.
        Assuming all are off.
        """
        start = 0,0
        end = 999,0
        expected = 1000
        lg = LightGrid(1000,1000)
        lg.toggle(start, end)
        self.assertEqual(lg.lights_on, expected)
        
    def test_toggle_lights02(self):
        """
        Toggle lights from 0,0 through 999,0.
        Assuming all are on.
        """
        start = 0,0
        end = 999,0
        expected = 999000
        lg = LightGrid(1000,1000)
        lg.on((0,0),(999,999))
        lg.toggle(start, end)
        self.assertEqual(lg.lights_on, expected)
        
    def test_toggle_lights03(self):
        """
        Toggle lights from 0,0 through 999,0.
        Assuming 500 are on.
        """
        start = 0,0
        half = 500,0
        end = 999,0
        expected = 499
        lg = LightGrid(1000,1000)
        lg.on(start, half)
        lg.toggle(start, end)
        self.assertEqual(lg.lights_on, expected)
        
    def test_turn_off_lights01(self):
        """
        Turn off lights from 499,499 through 500,500
        Assuming all are off.
        """
        start = 499,499
        end = 500,500
        expected = 0
        lg = LightGrid(1000,1000)
        lg.off(start,end)
        self.assertEqual(lg.lights_on, expected)

    def test_turn_off_lights02(self):
        """
        Turn off lights from 499,499 through 500,500
        Assuming all are on.
        """
        start = 499,499
        end = 500,500
        # Only 4 lights are off in a 2x2 grid
        expected = 999_996
        lg = LightGrid(1000,1000)
        lg.on((0,0),(999,999))
        lg.off(start,end)
        self.assertEqual(lg.lights_on, expected)

if __name__ == '__main__':
    unittest.main()
