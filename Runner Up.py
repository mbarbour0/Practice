n = int(input())
arr = map(int, input().split())
arr = set(arr)
arr = sorted(list(arr))

print(arr[-2])
