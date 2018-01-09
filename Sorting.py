s = 'Sorting1234'
odd = []
even = []
upper = []
lower = []
for i in s:
    if i.isalpha() == True:
        if i == i.upper():
            upper.append(i)
        elif i == i.lower():
            lower.append(i)
    else:
        if int(i) % 2 == 0:
            even.append(i)
        elif int(i) % 2 == 1:
            odd.append(i)

lower = ''.join(lower)
upper = ''.join(upper)
odd = ''.join(odd)
even = ''.join(even)

print lower + upper + odd + even

# output = ''.join(output)

# print output