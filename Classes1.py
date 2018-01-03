class Animal(object):
  def __init__(self, name):
    self.name = name
    
'''Assigning member variables to the class'''

class Animal(object):
  is_alive = True 
  """Assigning the member variable of is_alive = True 
  results in all objects of this class being assigned this value."""
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

'''Assigning more class objects'''

class Animal(object):
  is_alive = True
  health = 'good'
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Anderson", 36)
hippo.description()
sloth = Animal('Sleuth', 68)
ocelot = Animal('Oxtail', 42)

print hippo.health
print sloth.health
print ocelot.health

'''Practice initializing a Class, assigning it to a variable, and running a
Function from within the Class on the variable.'''

class ShoppingCart(object):
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

my_cart = ShoppingCart("Matt\'s")
my_cart.add_item("JIF Peanut Butter", 2.50)

'''Inherit a Derived Class from a Base Class'''

class Shape(object): #Base Class
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape): #Derived Class
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
'''Inheretance and reassigning a value from inheretance.'''

class Employee(object):
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00