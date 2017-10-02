from ffpicker.data.models import Season as stypes

class Schedule:
    def __init__(self, season, week, stype=stypes.REGULAR, data=''):
        self.season = season
        self.week = week
        self.stype = stype
        self.data = data

    def __str__(self):
        return self.data

    def save(self, filepath=None):
        default_filepath = '_'.join([str(self.season), self.stype, str(self.week)]) + '.txt'
        filepath = default_filepath if filepath is None else filepath
        with open(filepath, 'w') as outfile:
            outfile.write(self.data)
        print('saved schedule')
