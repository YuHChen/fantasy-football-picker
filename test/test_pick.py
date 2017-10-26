from ffpicker import pick

import itertools
import unittest

class TestPick(unittest.TestCase):
    def setUp(self):
        pass

    def test_between_givenOneTeamBias_returnBias(self):
        expected = 'giants'
        # test using combinations of team names and team codes
        for teams in itertools.product(['NYG', 'giants'], ['CHI', 'bears']):
            actual = pick.between(*teams).using(pick.team_bias).winner.name
            self.assertEqual(actual, expected)

    def test_between_givenBothTeamBiases_returnFirstBias(self):
        expected = 'giants'
        # test using combinations of team names and team codes
        for teams in itertools.product(['NYG', 'giants'], ['SEA', 'seahawks']):
            actual = pick.between(*teams).using(pick.team_bias).winner.name
            self.assertEqual(actual, expected)
