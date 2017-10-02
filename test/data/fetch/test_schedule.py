from ffpicker.data.models import Season as stypes
import ffpicker.data.fetch.sched as sched

import unittest

class TestSchedule(unittest.TestCase):
    def test_createScheduleUrl_givenPostSeasonWeek1_returnsUrlWithWeek18(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=18'.format(stypes.POST)
        actual = sched.create_schedule_url(0, stypes.POST, 1)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPostSeasonWeek4_returnsUrlWithWeek22(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=22'.format(stypes.POST)
        actual = sched.create_schedule_url(0, stypes.POST, 4)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPreSeasonWeek1_returnsUrlWithWeek1(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=1'.format(stypes.PRE)
        actual = sched.create_schedule_url(0, stypes.PRE, 1)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenProSeasonWeek1_returnsUrlWithWeek21(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=21'.format(stypes.PRO)
        actual = sched.create_schedule_url(0, stypes.PRO, 1)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenRegularSeasonWeek1_returnsUrlWithWeek1(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=1'.format(stypes.REGULAR)
        actual = sched.create_schedule_url(0, stypes.REGULAR, 1)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
