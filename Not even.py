import random

start = 5

def even_odd(number2):
    return not number2 % 2

while start > 0:
    number1 = random.randint(1,99)
    if even_odd(number1) == False:
        print("{} is odd".format(number1))
    elif even_odd(number1) == True:
        print("{} is even".format(number1))
    start -= 1