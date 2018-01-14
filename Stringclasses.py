import string

def stringcases(arg1):
    upperc = arg1.upper()
    lowerc = arg1.lower()
    titlec = string.capwords(arg1, ' ')
    reversec = list(arg1)
    reversec = reversec[-1::-1]
    reversec = ''.join(reversec)
    return(upperc, lowerc, titlec, reversec)
    
print(stringcases("Hey, my name is, what? My name is, Who? My name is tcka tcka Slim Shady."))