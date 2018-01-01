def median(lst):
  lst = sorted(lst)
  if len(lst) % 2 != 0:
    index = len(lst) // 2
    return lst[index]
  elif len(lst) % 2 == 0:
    index1 = (len(lst)/2) - 1
    index2 = len(lst)/2
    mean = (lst[index1] + lst[index2]) / 2.0
    return mean