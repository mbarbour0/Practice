def prime_numbers(arg1):
    primeset = []
    for i in arg1:
        value = True
        for item in range(2, int(i)):
            if i % item == 0:
                value = False
        if value == True:
            primeset.append(i)
    return primeset

print(prime_numbers(range(10000)))