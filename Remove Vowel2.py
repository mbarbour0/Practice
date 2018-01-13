def disemvowel(word):
    text = ""
    for letter in word:
        for i in "aeiouAEIOU":
            if letter == i:
                letter = ''
        text += letter
    return text