def onomoto(pattern):
    appresult = []
    for i in pattern:
        if i == ".":
            appresult.append("dot")
        if i == "_":
            appresult.append("dash")
    result = '-'.join(appresult)
    return result

print(onomoto(['.', '.', '.']))