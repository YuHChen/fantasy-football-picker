__all__ = [
    "Schedule",
    "Season"
]

class Season(object):
    POST = 'POST'
    PRE = 'PRE'
    PRO = 'PRO'
    REGULAR = 'REG'

class Schedule(object):
    """Data model of a season's week's schedule"""

    def __init__(self, season, week, stype=Season.REGULAR, data=None, games=None):
        self.season = season
        self.week = week
        self.stype = stype
        self.data = data
        self.games = games

    def __str__(self):
        return self.data if self.games is None else str(self.games)
