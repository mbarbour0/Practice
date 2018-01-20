import datetime
import pytz


pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')


fmt = "%Y-%m-%d %H:%M:%S %Z%z"
utc = pytz.utc


start = pacific.localize(datetime.datetime(2014, 4, 21, 9))
print(start)
print(start.strftime(fmt))


start_eastern = start.astimezone(eastern)
print(start_eastern)
print(start_eastern.strftime(fmt))


start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
print(start_utc.strftime(fmt))


start_pacific = start_utc.astimezone(pacific)
print(start_pacific)


apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)
print(apollo_13_eastern)


apollo_13_utc = apollo_13_eastern.astimezone(utc)
print(apollo_13_utc)
print(apollo_13_utc.astimezone(auckland).strftime(fmt))
print(apollo_13_utc.astimezone(mumbai).strftime(fmt))
print(apollo_13_utc.astimezone(eastern).strftime(fmt))
