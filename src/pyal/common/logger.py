from algorithm import is_none_or_empty, get_log_time
import pytz

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

    if is_none_or_empty(time_zone):
      self.set_US_pacific_time()
    else:
      self._country_city = time_zone

    self._level = 1

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
    return f"{self._class_name} {get_log_time(country_city=self._country_city)}"

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
