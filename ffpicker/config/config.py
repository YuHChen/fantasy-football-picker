import json, logging

class Config:
    _DEFAULT_CONFIG = {
        # schedules
        'SCHEDULE_DATA_DIR' : 'ffpicker-data/schedules',
        'SCHEDULE_RAW_DATA_DIR' : 'ffpicker-raw-data/schedules',
        'SCHEDULE_URL' : ('http://www.nfl.com/ajax/scorestrip?'
                          'season={}&seasonType={}&week={}'),
    }

    _CONFIG_FILENAME = 'config.json'

    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(Config.__name__)
        self._config = Config._DEFAULT_CONFIG
        # override default config with user defined config
        try:
            with open(Config._CONFIG_FILENAME, 'r') as config_file:
                user_defined_config = json.load(config_file)
                self._config = { **self._config, **user_defined_config }
        except FileNotFoundError:
            self._logger.info('No user defined config')
        except json.decoder.JSONDecodeError:
            message_format = ('Invalid JSON formatting in `%s`, '
                              'using default configuration settings instead')
            self._logger.warning(message_format, Config._CONFIG_FILENAME)

    def get_property(self, property_name):
        return self._config.get(property_name)
