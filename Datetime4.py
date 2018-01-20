import datetime



def minutes(arg1, arg2):
    return round(((arg2 - arg1).total_seconds())/60)

year = datetime.timedelta(days=365)
another_year = datetime.timedelta(weeks = 40, days = 84, hours = 23, minutes = 50, seconds = 600)
print(year)
print(year.total_seconds())
print(another_year)
print(another_year.total_seconds())
now = datetime.datetime.now()
nowsecond = now.second
print(nowsecond)