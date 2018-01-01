def remove_duplicates(i):
  if i == []:
    return []
  i = sorted(i)
  o = [i[0]]
  for value in i:
    if value > o[-1]:
      o.append(value)
  return o

print remove_duplicates([217, 1, 1, 1, 2, 3, 6, 2, 217, 4, 2, -23, -23])