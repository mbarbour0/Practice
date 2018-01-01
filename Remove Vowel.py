def anti_vowel(word):
  text = ''
  for c in word:
    for i in 'aeiouAEIOU':
      if c == i:
        c = ''
    text = text + c
  return text
print anti_vowel('welcome to the jam')