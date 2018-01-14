def split_and_join(line):
    result1 = line.split()
    result2 = "-".join(result1)
    return result2
    
print(split_and_join("Hi, my name is"))