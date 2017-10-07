from ffpicker.config.config import Config

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
