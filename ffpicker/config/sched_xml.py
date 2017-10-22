from ffpicker.config.config import Config

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
