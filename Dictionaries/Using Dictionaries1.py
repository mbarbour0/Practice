shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for i in food:
    if stock[i] >= 1:
      total += prices[i]
      stock[i] -= 1
      print 'The new amount of ' + str(i) + 's that we have is ' + str(stock[i])
    elif stock[i] == 0:
      print 'It looks like we are out of... ' + str(i) + 's'
  print 'We\'re going to need $' + str(total) + ' to ensure we can pay for our groceries.'
  return total

val1 = ['apple', 'banana', 'orange', 'orange', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana']

print compute_bill(val1)