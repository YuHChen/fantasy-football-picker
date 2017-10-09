from ffpicker.config import Config

import logging, os, unittest

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = True
        self.config = Config()

    def test_constructor_givenConfigFileDoesNotExist_shouldUseDefaultConfiguration(self):
        self.config._CONFIG_FILENAME = 'ffpicker-does-not-exist.json'
        config = Config()
        expected = 'ffpicker-data/schedules'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

    def test_constructor_givenInvalidConfigFile_shouldUseDefaultConfiguration(self):
        self.config._CONFIG_FILENAME = 'ffpicker-invalid.json'
        with open(self.config._CONFIG_FILENAME, 'w+') as config_file:
            config_file.write("")
        config = Config(self.logger)
        os.remove(config._CONFIG_FILENAME)
        expected = 'ffpicker-data/schedules'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

    def test_constructor_givenValidConfigFile_shouldUseUserDefinedConfiguration(self):
        self.config._CONFIG_FILENAME = 'ffpicker-valid.json'
        with open(self.config._CONFIG_FILENAME, 'w+') as config_file:
            config_file.write("{ \"SCHEDULE_DATA_DIR\" : \"success\" }")
        config = Config()
        os.remove(config._CONFIG_FILENAME)
        expected = 'success'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

    def test_constructor_shouldCreateInstancesWithSharedState(self):
        self.config._CONFIG_FILENAME = 'ffpicker-config.json'
        with open(self.config._CONFIG_FILENAME, 'w+') as config_file:
            config_file.write("{ \"SCHEDULE_DATA_DIR\" : \"first\" }")
        config = Config()
        with open(config._CONFIG_FILENAME, 'w') as config_file:
            config_file.write("{ \"SCHEDULE_DATA_DIR\" : \"second\" }")
        Config()
        os.remove(config._CONFIG_FILENAME)
        expected = 'second'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()



