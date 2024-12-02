from solution import reportlevels
import unittest



class TestReportLevels(unittest.TestCase):
    """2024 Day 2 Part 1
    This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.
    
    """
    
    def setUp(self):
        self.reportdata ="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        # Split the reportdata into a list of reports
        self.reports = self.reportdata.split('\n')

    def test_reportlevels(self):
        "7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[0])
        self.assertTrue(actual_report_is_safe)

    def test_reportlevels2(self):
        "1 2 7 8 9: Unsafe because 2 7 is an increase of 5."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[1])
        self.assertFalse(actual_report_is_safe)

    def test_reportlevels3(self):
        "9 7 6 2 1: Unsafe because 6 2 is a decrease of 4."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[2])
        self.assertFalse(actual_report_is_safe)

    def test_reportlevels4(self):
        "1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[3])
        self.assertFalse(actual_report_is_safe)

    def test_reportlevels5(self):
        "8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[4])
        self.assertFalse(actual_report_is_safe)

    def test_reportlevels6(self):
        "1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[5])
        self.assertTrue(actual_report_is_safe)

    def test_reportlevels7(self):
        "7 6 4 2 1: Safe without removing any level."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[0], problem_dampener_enabled=True)
        self.assertTrue(actual_report_is_safe)
    
    def test_reportlevels8(self):
        "1 2 7 8 9: Unsafe regardless of which level is removed."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[1], problem_dampener_enabled=True)
        self.assertFalse(actual_report_is_safe)
    
    def test_reportlevels9(self):
        "9 7 6 2 1: Unsafe regardless of which level is removed."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[2], problem_dampener_enabled=True)
        self.assertFalse(actual_report_is_safe)
    
    def test_reportlevels10(self):
        "1 3 2 4 5: Safe by removing the second level, 3."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[3], problem_dampener_enabled=True)
        self.assertTrue(actual_report_is_safe)

    def test_reportlevels11(self):
        "8 6 4 4 1: Safe by removing the third level, 4."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[4], problem_dampener_enabled=True)
        self.assertTrue(actual_report_is_safe)

    def test_reportlevels12(self):
        "1 3 6 7 9: Safe without removing any level."
        rl = reportlevels()
        actual_report_is_safe = rl.is_report_safe(self.reports[5], problem_dampener_enabled=True)
        self.assertTrue(actual_report_is_safe)