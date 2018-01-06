class BankAccount(object):
  error = 'Please enter a valid amount.'
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return 'This account belongs to: %s.\nYou currently have a balance of $%.02f' % (self.name, self.balance)
  
  def show_balance(self):
    print 'The balance in your account is $%.02f' % (self.balance)
  
  def deposit(self, amount):
    if amount <= 0:
      print error
    else:
      self.balance += amount
      print 'You are now depositing $%.02f. Your new balance is $%.02f' % (amount, self.balance)
  
  def withdraw(self, amount):
    if amount > self.balance:
      print 'You entered $%.02f. The current balance in your bank account is $%.02f Please enter an amount that is less than or equal to the amount in your bank account.' % (amount, self.balance)
    else:
      self.balance -= amount
      print 'You have withdrawn $%.02f. Your new balance is $%.02f.' % (amount, self.balance)
     
my_account = BankAccount('Matt')

print my_account
my_account.deposit(15000)
my_account.withdraw(5.25)
my_account.show_balance()
print my_account