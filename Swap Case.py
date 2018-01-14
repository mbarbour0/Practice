def swap_case(s):
    list1 = []
    for i in s:
        if i.lower() == i:
            list1.append(i.upper())
        elif i.upper() == i:
            list1.append(i.lower())
        else:
            list1.append(i)
    result = ''.join(list1)
    
    return result

print(swap_case("Hi, My Name is"))