import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(int1):
    return starter + datetime.timedelta(hours = int1)
