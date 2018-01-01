def reverse(word):
  word = str(word)
  count = len(word)
  for i in word:
    word[count] = i
    count -= 1
reverse('alskdfj')