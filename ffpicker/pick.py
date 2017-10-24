from ffpicker.config import PickConfig

__all__ = [
    "winner_between",
]

class PickContext(object):
    def __init__(self, team1, team2):
        self._team1 = team1
        self._team2 = team2

    @property
    def team1(self):
        return self._team1

    @property
    def team2(self):
        return self._team2

class Pick(object):
    def __init__(self, team1, team2):
        self._context = PickContext(team1, team2)
        self._winner = None

    def __str__(self):
        return str(self._winner)

    def using(self, pick_method):
        if self._winner is None:
            self._winner = pick_method(self._context)
        return self

def team_bias(pick_context):
    config = PickConfig()
    team_biases = config.team_biases
    for team in team_biases:
        if team == pick_context.team1 or team == pick_context.team2:
            return team

def winner_between(team1, team2):
    return Pick(team1, team2)
