from ffpicker.config import PickConfig
from ffpicker.data import models

import logging
import random

__all__ = [
    "between",
    "team_bias"
]

class PickContext(object):
    def __init__(self, team1, team2):
        self._team1 = models.team_from_str(team1)
        self._team2 = models.team_from_str(team2)

    @property
    def team1(self):
        return self._team1

    @property
    def team2(self):
        return self._team2

class PickResult(object):
    def __init__(self):
        self._team1_is_winner = None
        self._reasoning = None

    @property
    def is_team1_winner(self):
        return self._team1_is_winner

    @property
    def reason(self):
        return self._reasoning

    def because(self, reason):
        self._reasoning = reason
        return self

    def team1_wins(self):
        self._team1_is_winner = True
        return self

    def team2_wins(self):
        self._team1_is_winner = False
        return self

class Pick(object):
    def __init__(self, team1, team2):
        self._context = PickContext(team1, team2)
        self._finished_picking = False
        self._pick_methods = []
        self._pick_reasoning = []
        self._team1_is_winner = None

    def _pick(self):
        logger = logging.getLogger(__name__)
        if self._finished_picking: return

        for pick_method in self._pick_methods:
            logger.debug('Trying to pick using {}...'.format(pick_method.__name__))
            result = pick_method(self._context)
            if result is None:
                failed_message = '{} failed to pick a winner.'.format(pick_method.__name__)
                self._pick_reasoning.append(failed_message)
            else:
                self._team1_is_winner = result.is_team1_winner
                self._pick_reasoning.append(result.reason)
                self._finished_picking = True
                break

    @property
    def loser(self):
        self._pick()
        return self._context.team2 if self._team1_is_winner else self._context.team1

    @property
    def reason(self):
        def _indent(line):
            return '  * {}'.format(line)
        return '\n'.join([_indent(reason) for reason in self._pick_reasoning])

    @property
    def winner(self):
        self._pick()
        return self._context.team1 if self._team1_is_winner else self._context.team2

    def fallback(self, pick_method):
        return self.using(pick_method)

    def using(self, pick_method):
        self._pick_methods.append(pick_method)
        return self

def random_team(pick_context):
    reason = 'Randomly picked {} as the winner.'
    result1 = PickResult().team1_wins().because(reason.format(pick_context.team1))
    result2 = PickResult().team2_wins().because(reason.format(pick_context.team2))
    return random.choice([result1, result2])

def team_bias(pick_context):
    config = PickConfig()
    team_biases = [models.team_from_str(team_bias) for team_bias in config.team_biases]

    team1 = pick_context.team1
    team2 = pick_context.team2
    two_biases_reason = '{} is a bigger bias than {}.'
    one_bias_reason = '{} is one of the team biases, but {} is not.'
    for team in team_biases:
        if team is team1:
            reason = two_biases_reason if team2 in team_biases else one_bias_reason
            return PickResult().team1_wins().because(reason.format(team1, team2))
        if team is pick_context.team2:
            reason = two_biases_reason if team1 in team_biases else one_bias_reason
            return PickResult().team2_wins().because(reason.format(team2, team1))
    return None

def between(team1, team2):
    return Pick(team1, team2)
