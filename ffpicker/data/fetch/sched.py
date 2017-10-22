from ffpicker.config import ScheduleConfig
from ffpicker.data.models import Schedule
from ffpicker.data.models import Season as stypes
import ffpicker.data.transform as transform

import json, logging, os, urllib.request

_config = ScheduleConfig()

def _create_default_filepath(schedule, data_dir, ext='txt'):
    season = str(schedule.season)
    stype = schedule.stype
    week = str(schedule.week)
    filename = '{}.{}'.format('_'.join([season, stype, week]), ext)
    return os.path.join(data_dir, filename)

def _create_schedule_url(schedule):
    season = schedule.season
    stype = schedule.stype
    week = {
        stypes.POST: lambda x: x + 18 if (x == 4) else x + 17,
        stypes.PRE: lambda x: x,
        stypes.PRO: lambda x: x + 20,
        stypes.REGULAR: lambda x: x
    }[stype](schedule.week)
    return _config.url.format(season, stype, week)

def _load_schedule_from_json(season, week, stype, filepath=None):
    logger = logging.getLogger(__name__)
    schedule = Schedule(season, week, stype)
    filepath = _create_default_filepath(schedule, _config.data_dir, 'json') if filepath is None else filepath
    try:
        with open(filepath, 'r') as json_file:
            schedule_json = json.load(json_file)
            schedule.games = schedule_json['games']
    except FileNotFoundError:
        logger.info('Failed to load schedule from file: `%s`', filepath)
    except json.decoder.JSONDecodeError:
        logger.info('`%s` contains invalid JSON', filepath)
    return schedule

def _load_schedule_from_xml(season, week, stype, filepath=None):
    logger = logging.getLogger(__name__)
    schedule = Schedule(season, week, stype)
    filepath = _create_default_filepath(schedule, _config.raw_data_dir, 'xml') if filepath is None else filepath
    try:
        with open(filepath, 'r') as infile:
            schedule.data = infile.read()
    except FileNotFoundError:
        logger.info('Failed to load schedule from file: `%s`', filepath)
    return schedule

def _load_schedule(season, week, stype, filepath=None):
    schedule = _load_schedule_from_json(season, week, stype, filepath)
    if schedule.games is None:
        schedule = _load_schedule_from_xml(season, week, stype, filepath)
    if not schedule.data is None:
        transform.schedule_xml_to_json(schedule)
        _save_schedule_json(schedule)
        schedule = _load_schedule_from_json(season, week, stype, filepath)
    return schedule

def _save_schedule_json(schedule, filepath=None):
    logger = logging.getLogger(__name__)
    try:
        os.makedirs(_config.data_dir)
    except OSError:
        logger.info('Directory for schedule data already exists: `%s`',
                    _config.data_dir)
    filepath = _create_default_filepath(schedule, _config.data_dir, 'json') if filepath is None else filepath
    with open(filepath, 'w') as outfile:
        schedule_json = {
            'season' : schedule.season,
            'week' : schedule.week,
            'season_type' : schedule.stype,
            'games' : schedule.games
        }
        outfile.write(json.dumps(schedule_json, indent=2, sort_keys=True))

def _save_schedule_xml(schedule, filepath=None):
    logger = logging.getLogger(__name__)
    try:
        os.makedirs(_config.raw_data_dir)
    except OSError:
        logger.info('Directory for raw schedule data already exists: `%s`',
                    _config.raw_data_dir)
    filepath = _create_default_filepath(schedule, _config.raw_data_dir, 'xml') if filepath is None else filepath
    with open(filepath, 'w') as outfile:
        outfile.write(schedule.data)

def schedule(season, week, stype=stypes.REGULAR):
    logger = logging.getLogger(__name__)
    schedule = _load_schedule(season, week, stype)
    if schedule.data is None and schedule.games is None:
        logger.debug('Fetching schedule from...')
        schedule_url = _create_schedule_url(schedule)
        logger.debug('  %s', schedule_url)
        with urllib.request.urlopen(schedule_url) as response:
            schedule.data = response.read().decode('utf-8')
            _save_schedule_xml(schedule)
            schedule = transform.schedule_xml_to_json(schedule)
            _save_schedule_json(schedule)
    else:
        logger.debug('Fetched schedule from file')
    return schedule
