from ffpicker.data import transform
from ffpicker.data.models import Schedule
from ffpicker.data.models import Season as stypes

import unittest
import xml.etree.ElementTree as ET

class TestTransform(unittest.TestCase):
    def setUp(self):
        data = (
            '<ss>'
            '<gms gd="0" w="2" y="1" t="R">'
            '<g eid="0001010100" gsis="00000" d="Sun" t="1:00" q="F" k="" h="ARI" hnn="cardinals" hs="0" v="ATL" vnn="falcons" vs="0" p="" rz="" ga="" gt="REG"/>'
            '</gms>'
            '</ss>'
        )
        self.schedule = Schedule(1, 2, data=data)

    def test_gameXmlToJson(self):
        game_xml = ET.fromstring(self.schedule.data).find('gms').find('g')
        expected = {
            'day' : 'Sun',
            'event_id' : '0001010100',
            'home' : 'ARI',
            'home_name' : 'cardinals',
            'home_score' : '0',
            'season_type' : 'REG',
            'time' : '1:00',
            'visitor' : 'ATL',
            'visitor_name' : 'falcons',
            'visitor_score' : '0'
        }
        actual = transform._game_xml_to_json(game_xml)
        self.assertEqual(actual, expected)

    def test_gameXmlToJson_givenRegularSeasonData_raisesRuntimeError(self):
        game_xml = ET.fromstring(self.schedule.data).find('gms').find('g')
        with self.assertRaisesRegex(RuntimeError, 'PRE season.*REG season'):
            transform._game_xml_to_json(game_xml, stypes.PRE)

    def test_scheduleXmlToJson_givenSeason2_raisesRuntimeError(self):
        self.schedule.season = 2
        with self.assertRaisesRegex(RuntimeError, '2 season.*1 season'):
            transform.schedule_xml_to_json(self.schedule)

    def test_scheduleXmlToJson_givenWeek3_raisesRuntimeError(self):
        self.schedule.week = 3
        with self.assertRaisesRegex(RuntimeError, 'week 3.*week 2'):
            transform.schedule_xml_to_json(self.schedule)
