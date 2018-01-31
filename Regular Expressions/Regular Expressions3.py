import re


print(re.findall(r'''
    \b@[-\w\d+.]* # First a word boundary, an @, and then any number of characters
    [^gov\t]+ # Ignore 1 or more instances of the letter 'g', 'o', or 'v' and a tab.
    \b #Match another word boundary
    ''', data, re.VERBOSE|re.I))


print(re.findall(r"""
    \b[-\w]+,
    \s
    [-\w ]+
    [^\t\n]
""", data, re.X))


string = '1234567890'


good_numbers = re.findall(r'[^567]', string)


line = re.compile(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)
print(line.search(data).groupdict())



print(line)
print(line.groupdict())


string = 'Perotto, Pier Giorgio'
names = re.match(r'([-\w ]*),\s([-\w ]+)', string)


string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''(?P<email>[-\w\d.+]+@[-\w\d.]+).\s
    (?P<phone>\(?\d{3}\)?\s?-?\d{3}-?\d{4})''', string, re.X|re.I)


twitters = re.search(r'(?P<twitter>@[\w\d]+)$', string, re.M)