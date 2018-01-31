import datetime

start = datetime.datetime.now()
start = start.replace(hour = 9, minute = 0, second = 0, microsecond = 0)
timed = start - datetime.datetime.now()
hours_worked = round(timed.seconds/3600, 2)




print(start)
print(datetime.datetime.now())
print(timed)
print(timed.days)
#print(timed.hours)
print(timed.seconds)
print(timed.microseconds)
print(hours_worked)
