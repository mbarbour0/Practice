def combo(a, b):
    return list(zip(a,b))

print(combo([1,2,3], 'abc'))

def combo(arg1, arg2):
    tpl_list = list()
    for index, element in enumerate(arg1):
        tpl_list.append((arg1[index], arg2[index]))
    return tpl_list
print(combo([1,2,3], 'abc'))