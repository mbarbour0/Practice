import re


names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()


print(re.search(r'\(?\d{3}\)? \d{3}-\d{4}', data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))


print(re.search(r'\w*, \w*', data))
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))


print(re.findall(r'\b[trehous]{9}\b', data, re.I))


def find_words(count1, str1):
    return re.findall(r'\w{' + str(count1) + ',}', str1)
