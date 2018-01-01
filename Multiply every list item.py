def product(numbers):
  result = numbers[0]
  for i in numbers[1:]:
    result *= i
  return result

print product([5, 3, 2])