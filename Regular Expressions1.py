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

"""
\w : any Unicode character
\W : anything that isn't a Unicode character
\s : any whitespace
\S : anything that isn't whitespace
\d : any number from 0 to 9
\D : anything that isn't a number
\b : word boundaries or edges of a word
\B : anything that isn't the edge of a word
\t : tab


{3} : something that occurs exactly 3 times
{,3} : something that occurs 0 to 3 times
{3,} : something that occurs 3 or more times
{3,5} : something that occurs 3, 4, or 5 times
? : something that occurs 0 or 1 times
* : something that occurs at least 0 times
+ : something that occurs at least once


[aple] : finds apple (you can leave out duplicates)
[a-z] : any lowercase letters from a - z
[^2] : anything that is not 2


"""
