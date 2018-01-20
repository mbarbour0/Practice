import datetime

def timestamp_oldest(*args):
    """Use POIX Timestamp format to find the earliest date and return it"""
    result = []
    for i in args:
        result.append(i)
    result.sort()
    return datetime.datetime.fromtimestamp(result[0])

print(timestamp_oldest(1361446545, 1361446323))