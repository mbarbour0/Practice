import datetime

# def time_machine(arg1):
    # return datetime.datetime.strptime(arg1, '%M %H %d %y')

# print(time_machine('12 11 20 18'))

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(lentime, measure):
    now = datetime.datetime.now()
    if measure.lower() == 'minutes':
        return now + datetime.timedelta(minutes = lentime)
    elif measure.lower() == 'hours':
        return now + datetime.timedelta(hours = lentime)
    elif measure.lower() == 'days':
        return now + datetime.timedelta(days = lentime)
    elif measure.lower() == 'years':
        return now + datetime.timedelta(days = 365*lentime)
    
    # return datetime.datetime.strptime(arg1, '%M %H %d %y')
    
print(time_machine(5, 'minutes'))
print(time_machine(5, 'hours'))
print(time_machine(5, 'days'))
print(time_machine(5, 'years'))