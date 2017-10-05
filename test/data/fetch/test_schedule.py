from ffpicker.data.models import Schedule as Schedule
from ffpicker.data.models import Season as stypes
import ffpicker.data.fetch.sched as sched

import unittest

class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule(0, 1)

    def test_createScheduleUrl_givenPostSeasonWeek1_returnsUrlWithWeek18(self):
        self.schedule.stype = stypes.POST
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=18'.format(stypes.POST)
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPostSeasonWeek4_returnsUrlWithWeek22(self):
        self.schedule.stype = stypes.POST
        self.schedule.week = 4
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=22'.format(stypes.POST)
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPreSeasonWeek1_returnsUrlWithWeek1(self):
        self.schedule.stype = stypes.PRE
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=1'.format(stypes.PRE)
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenProSeasonWeek1_returnsUrlWithWeek21(self):
        self.schedule.stype = stypes.PRO
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=21'.format(stypes.PRO)
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenRegularSeasonWeek1_returnsUrlWithWeek1(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType={}&week=1'.format(stypes.REGULAR)
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
