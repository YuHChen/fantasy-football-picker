from ffpicker.config import ScheduleXMLConfig
from ffpicker.data.models import Schedule
from ffpicker.data.models import Season as stypes

import logging, os
import xml.etree.ElementTree as ET

_config = ScheduleXMLConfig()

def _game_xml_to_json(game_xml, stype=stypes.REGULAR):
    season_type = game_xml.get(_config.season_type)
    if stype != season_type:
        err_msg = ('Expected {} season game, '
                   'but found data for {} season game.')
        raise RuntimeError(err_msg.format(stype, season_type))

    game_json = {
        'day' : game_xml.get(_config.day),
        'event_id' : game_xml.get(_config.event_id),
        'home' : game_xml.get(_config.home),
        'home_name' : game_xml.get(_config.home_name),
        'home_score' : game_xml.get(_config.home_score),
        'season_type' : season_type,
        'time' : game_xml.get(_config.time),
        'visitor' : game_xml.get(_config.visitor),
        'visitor_name' : game_xml.get(_config.visitor_name),
        'visitor_score' : game_xml.get(_config.visitor_score)
    }
    return game_json

def schedule_xml_to_json(schedule):
    logger = logging.getLogger(__name__)
    schedule_json = {}
    schedule_xml = ET.fromstring(schedule.data)
    games = schedule_xml.find(_config.games)
    week = int( games.get(_config.week))
    year = int(games.get(_config.year))
    if (schedule.week != week or schedule.season != year):
        err_msg = ('Expected schedule data for {} season week {}, '
                   'but found data for {} season week {}.')
        raise RuntimeError(err_msg.format(schedule.season, schedule.week, year, week))
    schedule.games = [_game_xml_to_json(game, schedule.stype) for game in games]
    return schedule
