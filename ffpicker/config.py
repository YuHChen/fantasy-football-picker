import json
import logging

__all__ = [
    "Config",
    "PickConfig",
    "ScheduleConfig",
    "ScheduleXMLConfig"
]

class Config(object):
    _shared_state = {
        '_DEFAULT_CONFIG' : {
            # pick
            'PICK_TEAM_BIASES' : [
                'NYG', 'giants',
                'NYJ', 'jets',
                'SEA', 'seahawks'
            ],

            # schedules
            'SCHEDULE_DATA_DIR' : 'ffpicker-data/schedules',
            'SCHEDULE_RAW_DATA_DIR' : 'ffpicker-raw-data/schedules',
            'SCHEDULE_URL' : ('http://www.nfl.com/ajax/scorestrip?'
                              'season={}&seasonType={}&week={}'),
            # schedule XML
            'SCHEDULE_XML_DAY' : 'd',
            'SCHEDULE_XML_EVENT_ID' : 'eid',
            'SCHEDULE_XML_GAME' : 'g',
            'SCHEDULE_XML_GAMES' : 'gms',
            'SCHEDULE_XML_HOME' : 'h',
            'SCHEDULE_XML_HOME_NAME' : 'hnn',
            'SCHEDULE_XML_HOME_SCORE' : 'hs',
            'SCHEDULE_XML_SEASON_TYPE' : 'gt',
            'SCHEDULE_XML_TIME' : 't',
            'SCHEDULE_XML_VISITOR' : 'v',
            'SCHEDULE_XML_VISITOR_NAME' : 'vnn',
            'SCHEDULE_XML_VISITOR_SCORE' : 'vs',
            'SCHEDULE_XML_WEEK' : 'w',
            'SCHEDULE_XML_YEAR' : 'y'
        },
        '_CONFIG_FILENAME' : 'config.json'
    }

    def __new__(cls, *p, **k):
        self = object.__new__(cls)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(Config.__name__)
        self._config = self._DEFAULT_CONFIG
        # override default config with user defined config
        try:
            with open(self._CONFIG_FILENAME, 'r') as config_file:
                user_defined_config = json.load(config_file)
                self._config = { **self._config, **user_defined_config }
        except FileNotFoundError:
            self._logger.info('No user defined config')
        except json.decoder.JSONDecodeError:
            message_format = ('Invalid JSON formatting in `%s`, '
                              'using default configuration settings instead')
            self._logger.warning(message_format, self._CONFIG_FILENAME)

    def get_property(self, property_name):
        return self._config.get(property_name)

class PickConfig(Config):
    @property
    def team_biases(self):
        return self.get_property('PICK_TEAM_BIASES')

class ScheduleConfig(Config):
    @property
    def url(self):
        return self.get_property('SCHEDULE_URL')

    @property
    def data_dir(self):
        return self.get_property('SCHEDULE_DATA_DIR')

    @property
    def raw_data_dir(self):
        return self.get_property('SCHEDULE_RAW_DATA_DIR')

class ScheduleXMLConfig(Config):
    @property
    def day(self):
        return self.get_property('SCHEDULE_XML_DAY')

    @property
    def event_id(self):
        return self.get_property('SCHEDULE_XML_EVENT_ID')

    @property
    def game(self):
        return self.get_property('SCHEDULE_XML_GAME')

    @property
    def games(self):
        return self.get_property('SCHEDULE_XML_GAMES')

    @property
    def home(self):
        return self.get_property('SCHEDULE_XML_HOME')

    @property
    def home_name(self):
        return self.get_property('SCHEDULE_XML_HOME_NAME')

    @property
    def home_score(self):
        return self.get_property('SCHEDULE_XML_HOME_SCORE')

    @property
    def season_type(self):
        return self.get_property('SCHEDULE_XML_SEASON_TYPE')

    @property
    def time(self):
        return self.get_property('SCHEDULE_XML_TIME')

    @property
    def visitor(self):
        return self.get_property('SCHEDULE_XML_VISITOR')

    @property
    def visitor_name(self):
        return self.get_property('SCHEDULE_XML_VISITOR_NAME')

    @property
    def visitor_score(self):
        return self.get_property('SCHEDULE_XML_VISITOR_SCORE')

    @property
    def week(self):
        return self.get_property('SCHEDULE_XML_WEEK')

    @property
    def year(self):
        return self.get_property('SCHEDULE_XML_YEAR')
