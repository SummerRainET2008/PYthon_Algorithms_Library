import pytz
import datetime

class Logger:
  DEBUG = 0
  INFO  = 1
  WARRNING = 2
  ERROR = 3

  def __init__(self, class_or_str, time_zone: str=""):
    if isinstance(class_or_str, str):
      self._class_name = class_or_str
    else:
      self._class_name = class_or_str.__class__.__name__

    if time_zone == None or time_zone == "":
      self.set_US_pacific_time()
    else:
      self._country_city = time_zone

    self._level = 1

  def _strdate(self, timezone: str, now):
    city = timezone.split("/")[-1]
    ts = now.strftime("%Y-%m-%d_%Ih-%Mm-%Ss_%p")
    return f"{city}_{ts}"

  def _get_log_time(self, utc_time: bool = True, country_city: str = None):
    '''
    utc_time: if False, return local time(server);
              if True, return local time(city).
    country_city : When utc_time is true,  if city is None, return UTC(0).
                  See pytz/__init__.py:510, all_timezones

    e.g., SF time is UTC+8, then get_log_time(True) - 8 = get_log_time(False)
    '''
    if utc_time:
      if country_city == None or country_city == "":
        now = datetime.datetime.utcnow()
        return self._strdate("utc", now)
      else:
        now = datetime.datetime.now(pytz.timezone(country_city))
        return self._strdate(country_city, now)

    else:
      now = datetime.datetime.now()
      return self._strdate("local", now)

  def set_timezone_or_city(self, timezone_or_city):
    self._country_city = timezone_or_city

  def set_BeiJing_time(self):
    self._country_city = "Asia/Shanghai"

  def set_US_pacific_time(self):
    self._country_city = "America/Los_Angeles"

  def set_US_eastern_time(self):
    self._country_city = "US/Eastern"

  def get_avaialable_timezone_or_cities(self):
    return pytz.all_timezones_set

  def set_level(self, level: int):
    self._level = level

  def is_debug(self):
    return self._level <= 0

  def _title(self):
    return f"{self._class_name} {self._get_log_time(country_city=self._country_city)}"

  def debug(self, *args):
    if self._level <= self.DEBUG:
      print(self._title(), "DEBUG:", *args)

  def info(self, *args):
    if self._level <= self.INFO:
      print(self._title(), "INFO:", *args)

  def warn(self, *args):
    if self._level <= self.WARRNING:
      print(self._title(), "WARN:", *args)

  def error(self, *args):
    if self._level <= self.ERROR:
      print(self._title(), "ERR:", *args)
