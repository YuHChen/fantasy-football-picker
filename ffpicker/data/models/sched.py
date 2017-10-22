from ffpicker.data.models import Season as stypes

class Schedule:
    """Data model of a season's week's schedule"""

    def __init__(self, season, week, stype=stypes.REGULAR, data=None, games=None):
        self.season = season
        self.week = week
        self.stype = stype
        self.data = data
        self.games = games

    def __str__(self):
        return self.data if self.games is None else str(self.games)
