def combiner(arg1):
    result = ''
    count = 0
    for i in arg1:
        if isinstance(i, (float, int)) == True:
            count += i
        elif isinstance(i, str) == True:
            result += i
    return result + str(count)

print(combiner(["cat", 52, "alpha", 65.4, 128, "hotdog"]))