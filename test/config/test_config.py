from ffpicker.config import Config

import os, unittest

class TestConfig(unittest.TestCase):
    def test_constructor_givenConfigFileDoesNotExist_shouldUseDefaultConfiguration(self):
        Config._CONFIG_FILENAME = 'ffpicker-does-not-exist.json'
        config = Config()
        expected = 'ffpicker-data/schedules'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

    def test_constructor_givenInvalidConfigFile_shouldUseDefaultConfiguration(self):
        Config._CONFIG_FILENAME = 'ffpicker-invalid.json'
        with open(Config._CONFIG_FILENAME, 'w+') as config_file:
            config_file.write("")
        config = Config()
        os.remove(Config._CONFIG_FILENAME)
        expected = 'ffpicker-data/schedules'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

    def test_constructor_givenValidConfigFile_shouldUseUserDefinedConfiguration(self):
        Config._CONFIG_FILENAME = 'ffpicker-valid.json'
        with open(Config._CONFIG_FILENAME, 'w+') as config_file:
            config_file.write("{ \"SCHEDULE_DATA_DIR\" : \"success\" }")
        config = Config()
        os.remove(Config._CONFIG_FILENAME)
        expected = 'success'
        actual = config.get_property('SCHEDULE_DATA_DIR')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()



