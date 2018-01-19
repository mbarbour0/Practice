result = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    result.append((name, score))

a, b, c = enumerate(result)

for enum, grads in result:
    for nme, grd in grads:
        
        

print(a, b, c)
