import re


string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''


players = re.match(r'''
    (?P<last_name>[\w ]*),\s
    (?P<first_name>[\w ]*):\s
    (?P<score>[\d]*)?
''', string, re.MULTILINE|re.X)


line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)


# print(line)
# print(line.search(data).groupdict())


for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
    