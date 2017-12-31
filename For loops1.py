def why_me(x):
  total = 1
  neg = -1
  for i in x:
    if i > 0:
      total += i
    else:
      neg += i
  return total, neg
      
val1 = [1, 2, 3]
val2 = [-9, 1000000, 356, -92]

print (why_me(val2))


