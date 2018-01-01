def factorial(x):
  fact = x
  while x > 1:
    fact *= (x-1)
    x -= 1
  return fact

print factorial(10000)