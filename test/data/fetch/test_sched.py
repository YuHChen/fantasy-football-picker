from ffpicker.data.models import Schedule as Schedule
from ffpicker.data.models import Season as stypes
import ffpicker.data.fetch.sched as sched

import unittest

class TestSched(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule(0, 1)

    def test_createDefaultFilepath_givenPostSeasonWeek1(self):
        self.schedule.stype = stypes.POST
        expected = 'ffpicker-raw-data/schedules/0_POST_1.txt'
        actual = sched._create_default_filepath(self.schedule)
        self.assertEqual(actual, expected)

    def test_createDefaultFilepath_givenPreSeasonWeek1(self):
        self.schedule.stype = stypes.PRE
        expected = 'ffpicker-raw-data/schedules/0_PRE_1.txt'
        actual = sched._create_default_filepath(self.schedule)
        self.assertEqual(actual, expected)

    def test_createDefaultFilepath_givenProSeasonWeek1(self):
        self.schedule.stype = stypes.PRO
        expected = 'ffpicker-raw-data/schedules/0_PRO_1.txt'
        actual = sched._create_default_filepath(self.schedule)
        self.assertEqual(actual, expected)

    def test_createDefaultFilepath_givenRegularSeasonWeek1(self):
        self.schedule.stype = stypes.REGULAR
        expected = 'ffpicker-raw-data/schedules/0_REG_1.txt'
        actual = sched._create_default_filepath(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPostSeasonWeek1_returnsUrlWithWeek18(self):
        self.schedule.stype = stypes.POST
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType=POST&week=18'
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPostSeasonWeek4_returnsUrlWithWeek22(self):
        self.schedule.stype = stypes.POST
        self.schedule.week = 4
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType=POST&week=22'
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenPreSeasonWeek1_returnsUrlWithWeek1(self):
        self.schedule.stype = stypes.PRE
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType=PRE&week=1'
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenProSeasonWeek1_returnsUrlWithWeek21(self):
        self.schedule.stype = stypes.PRO
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType=PRO&week=21'
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

    def test_createScheduleUrl_givenRegularSeasonWeek1_returnsUrlWithWeek1(self):
        expected = 'http://www.nfl.com/ajax/scorestrip?season=0&seasonType=REG&week=1'
        actual = sched._create_schedule_url(self.schedule)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
