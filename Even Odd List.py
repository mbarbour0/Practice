def solution(list1, int1):
    empt = []
    for i in list1:
        if i in empt:
            empt.remove(i)
        else:
            empt.append(i)
    return int(empt[0])

print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 10], 13))