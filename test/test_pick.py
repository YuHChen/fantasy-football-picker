from ffpicker import pick

import unittest

class TestPick(unittest.TestCase):
    def setUp(self):
        pass

    def test_winnerBetween_givenOneTeamBias_returnBias(self):
        expected = 'giants'
        actual = str(pick.winner_between('giants', 'bears').using(pick.team_bias))
        self.assertEqual(actual, expected)

    def test_winnerBetween_givenBothTeamBiases_returnFirstBias(self):
        expected = 'giants'
        actual = str(pick.winner_between('seahawks', 'giants').using(pick.team_bias))
        self.assertEqual(actual, expected)
