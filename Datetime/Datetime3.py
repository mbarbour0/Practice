import datetime

now = datetime.datetime.now()
today = datetime.datetime.today()

print(today)

today = datetime.datetime.combine(datetime.date.today(), datetime.time())

todaymonth = today.month
todayhour = today.hour
todayyear = today.year
nowhour = now.hour

print(now)
print(today)
print(todaymonth)
print(todayhour)
print(todayyear)
print(nowhour)
