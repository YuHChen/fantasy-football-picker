import json, logging

class Config(object):
    _shared_state = {
        '_DEFAULT_CONFIG' : {
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
