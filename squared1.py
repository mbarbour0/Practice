def squared(num):
    try:
        num = int(num)
        print(num ** 2)
    except ValueError:
        print(num * len(num))

squared(5)
squared("2")
squared("tim")