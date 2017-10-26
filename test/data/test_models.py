from ffpicker.data import models

import unittest

class TestModels(unittest.TestCase):
    def setUp(self):
        pass

    def test_teamFromStr_givenTeamCode_returnsSameTeamGivenTeamName(self):
        expected = models.team_from_str('NYG')
        actual = models.team_from_str('giants')
        self.assertIs(actual, expected)

    def test_teamFromStr_givenInvalidTeamCode_raisesRuntimeError(self):
        with self.assertRaisesRegex(RuntimeError, 'ABC'):
            models.team_from_str('ABC')

    def test_teamFromStr_givenInvalidTeamName_raisesRuntimeError(self):
        with self.assertRaisesRegex(RuntimeError, 'not-a-valid-team-name'):
            models.team_from_str('not-a-valid-team-name')
