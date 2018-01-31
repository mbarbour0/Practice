import datetime

def time_tango(date, time):
    result = date + " " + time
    res1 = datetime.datetime.strptime(result, '%m/%d/%Y %H %M %S')
    return res1
    # result = datetime.datetime.strftime

def ttime_tango(date, time): 
   return datetime.datetime.combine(date, time)
    
print(time_tango('1/20/2018', '0 19 13'))