import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)

pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)

pytz_string = local.strftime(fmt)
