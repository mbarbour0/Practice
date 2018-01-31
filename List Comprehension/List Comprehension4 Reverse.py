"""Reverse a list"""

my_list = range(1, 10)

my_list = my_list[::-1] #You're able to rewrite a list backwards with this

print my_list

"""Reversing a list and counting backwards"""

to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10] # Reversing list by 10

print backwards_by_tens

"""Iterating through a range of 1 to 15 and only returning those
numbers divisible by 3 or 5"""

threes_and_fives = [i for i in range(1, 16) if (i % 3 == 0) or (i % 5 == 0)]

print threes_and_fives

"""List comprehension to iterate through a range and square the results,
then only display results from that result if it is between 30 and 70."""

squares = [i ** 2 for i in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)