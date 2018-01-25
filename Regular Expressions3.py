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


line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', data, re.X|re.M)


print(line)
print(line.groupdict())
