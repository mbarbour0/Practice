import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)

pacific = datetime.timezone(datetime.timedelta(hours = -8))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo = pacific)

newzone = datetime.timezone(datetime.timedelta(hours = 1))
paris = hill_valley.astimezone(newzone)
