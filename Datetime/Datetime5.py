import datetime

now = datetime.datetime.now()

print(now.strftime('%B %d'))
print(now.strftime('%m/%d/%y'))
print(now.strftime("%m, %d, %Y"))

birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')
birthday_party = datetime.datetime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')

print(birthday)
print(birthday_party)

def to_string(arg1):
    return datetime.datetime.strftime(arg1, '%d %B %Y')

def from_string(arg1, arg2):
    return datetime.datetime.strptime(arg1, arg2)