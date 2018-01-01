def censor(text, word):
  words = text.split()
  count = 0
  result = ''
  stars = '*' * len(word)
  for i in words:
    if i == word:
      words[count] = stars
    count += 1
  result = ' '.join(words)
  return result

print censor('hey hey what can i do?', 'hey')