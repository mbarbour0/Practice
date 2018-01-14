import string 
print(string.capwords(input(), ' '))

def capitalize(string):
    list1 = string.split()
    list2 = []
    for i in list1:
        list3 = list(i)
        list3[0] = list3[0].upper()
        list3 = ''.join(list3)
        list2.append(list3)
    list2 = ' '.join(list2)
    return list2
print(capitalize("hello world"))