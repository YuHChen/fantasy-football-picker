__all__ = [
    "Schedule",
    "Season",
    "Team",
    "team_from_str"
]

class Season(object):
    """Data model of types of seasons"""
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

class Team(object):
    """Data model of a team"""

    def __init__(self, code, name):
        self._code = code
        self._name = name

    def __str__(self):
        return '{} ({})'.format(self._name, self._code)

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

_STR_TO_TEAM_MAPPING = {}
_TEAM_METADATA = [
    ('SF', '49ers'),
    ('CHI', 'bears'),
    ('CIN', 'bengals'),
    ('BUF', 'bills'),
    ('DEN', 'broncos'),
    ('CLE', 'browns'),
    ('TB', 'buccaneers'),
    ('ARI', 'cardinals'),
    ('LAC', 'chargers'),
    ('KC', 'chiefs'),
    ('IND', 'colts'),
    ('DAL', 'cowboys'),
    ('MIA', 'dolphins'),
    ('PHI', 'eagles'),
    ('ATL', 'falcons'),
    ('NYG', 'giants'),
    ('JAX', 'jaguars'),
    ('NYJ', 'jets'),
    ('DET', 'lions'),
    ('GB', 'packers'),
    ('CAR', 'panthers'),
    ('OAK', 'raiders'),
    ('LA', 'rams'),
    ('BAL', 'ravens'),
    ('WAS', 'redskins'),
    ('NO', 'saints'),
    ('SEA', 'seahawks'),
    ('PIT', 'steelers'),
    ('HOU', 'texans'),
    ('TEN', 'titans'),
    ('NE', 'patriots'),
    ('MIN', 'vikings')
]
for team_metadatum in _TEAM_METADATA:
    team = Team(*team_metadatum)
    _STR_TO_TEAM_MAPPING[team_metadatum[0]] = team
    _STR_TO_TEAM_MAPPING[team_metadatum[1]] = team

def team_from_str(team_str):
    team = _STR_TO_TEAM_MAPPING.get(team_str)
    if team is None:
        raise RuntimeError('No team with code or name of `{}`'.format(team_str))
    return team
