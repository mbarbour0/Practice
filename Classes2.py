class Customer(object):
    def __init__(self, name, age, phone_number, customer_id, state):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.customer_id = customer_id
        self.state = state
    def status(self, prospect):
        self.prospect = prospect
        if prospect != 'n' or prospect != 'y':
            return 'y'
        else:
            return prospect
        
class Transitioned(Customer):
    def status(self, prospect):
        self.prospect = prospect
        if prospect != 'n' or prospect != 'y' or prospect != 'd':
            return 'y'
        else:
            return prospect

alfred = Transitioned('Alfred', 18, 7044561231, 111222333, 'nc')
print alfred.status('d')

alfred = Customer('Alfred', 18, 7044561231, 111222333, 'nc')


'''
Checking if a triangle's angles = 180 with a class

'''

class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
    
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    
my_triangle = Triangle(90, 30, 60)

print my_triangle.number_of_sides
print my_triangle.check_angles()