# This program will help you in maths

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is now starting, prepare to di... ahem, prepare to have me help you human master"

print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting.."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = pi * (radius ** 2)
  print "The pie is baking..."
  sleep(1)
  print "%.2f" % (area) + "\n" + hint
elif option == "T":
  base = float(raw_input("Please enter the base "))
  height = float(raw_input("Please enter the height "))
  area = 0.5 * base * height
  print "Uni Bi Tri..."
  sleep(1)
  print "%.2f" % (area) + "\n" + hint
else:
  print "You've entered garbage, son. I'm closing this project down..."
