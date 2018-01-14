def multiply(*args):
    product = args[0]
    for i in args[1:]:
        product *= i
    return product

print(multiply(1, 2, 3, 4 , 5, 6))