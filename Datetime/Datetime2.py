import datetime

now = datetime.datetime.now()
now3hours = now + datetime.timedelta(hours = 3)
now3days = now + datetime.timedelta(days = 3)
nowminus3days = now - datetime.timedelta(days = 3)
nowdate = now.date()
nowtime = now.time()
hour = datetime.timedelta(hours=1)
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0) + datetime.timedelta(days = 1)
timeofftomorrow = tomorrow + workday
appointment = datetime.timedelta(minutes = 45)
start = datetime.datetime(2018, 11, 1, 3, 0)
end = start + appointment





print(now)
print(now3hours)
print(now3days)
print(nowminus3days)
print(nowdate)
print(nowtime)
print(hour)
print(workday)
print(tomorrow)
print(timeofftomorrow)
print(appointment)
print(start)
print(end)
