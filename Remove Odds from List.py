def remove_odds(numbers):
  result = []
  for i in numbers:
    if i % 2 == 0:
      result.append(i)
  return result