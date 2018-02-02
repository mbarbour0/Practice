n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for items in lists:
    for i in items:
      results.append(i)
  return results

print flatten(n)