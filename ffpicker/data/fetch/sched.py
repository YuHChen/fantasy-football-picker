from ffpicker.data.models import Schedule
from ffpicker.data.models import Season as stypes

import urllib.request

SCHEDULE_URL_FORMAT = 'http://www.nfl.com/ajax/scorestrip?season={}&seasonType={}&week={}'
        
def create_schedule_url(season, stype, week):
    week = {
        stypes.POST: lambda x: x + 18 if (x == 4) else x + 17,
        stypes.PRE: lambda x: x,
        stypes.PRO: lambda x: x + 20,
        stypes.REGULAR: lambda x: x
    }[stype](week)
    return SCHEDULE_URL_FORMAT.format(season, stype, week)

def schedule(season, week, stype=stypes.REGULAR):
    print("Fetching schedule from...")
    schedule_url = create_schedule_url(season, stype, week)
    print('  ' + schedule_url)
    data = 'Result schedule'
    with urllib.request.urlopen(schedule_url) as response:
        data = response.read().decode('utf-8')
    schedule = Schedule(season, week, stype)
    schedule.data = data
    return schedule
