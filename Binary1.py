def solution(N):
    count = 0
    empt = []
    res = str(bin(N))
    for i in res[2:]:
        if i == "0":
            count += 1
        elif i != "0":
            empt.append(count)
            count = 0
    return max(empt)

print(solution(1041))
print(solution(15))