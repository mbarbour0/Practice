import re


names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()


last_name = r'Love'
first_name = r'Kenneth'
print(re.match(last_name, data))
print(re.search(first_name, data))


file_object = open('basics.txt')
data = file_object.read()
file_object.close()


first = re.match(r'Four', data)
liberty = re.search(r'Liberty', data)


def first_number(arg1):
    return re.search(r'\d', arg1)

def numbers(int1, str1):
    return re.search(r'\d' * int1, str1)
