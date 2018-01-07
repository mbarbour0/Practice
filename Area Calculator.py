# Area Calculator

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print 'Your area calculator is now starting up...'

print 'The current time is %02d/%02d/%04d %02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = 'Don\'t forget to include the correct units! \nExiting...'

option = raw_input('Enter C for Circle or T for Triangle: ')
option = option.upper()

if option == 'C':
  radius = float(raw_input('Input a Radius for your Circle: '))
  area = pi * (radius ** 2)
  print 'The pie is baking...'
  sleep(1)
  print 'The Area of your Circle is %.02f.' % (area) + ' ' + hint
elif option == 'T':
  base = float(raw_input('Enter a Base for your Triangle: '))
  height = float(raw_input('Enter a Height for your Triangle: '))
  area = .5 * base * height
  print 'Uni Bi Tri...'
  sleep(1)
  print 'The area of your Triangle is %.02f.' % (area) + ' ' + hint
else:
  print 'You\'ve entered hot garbagio, please try again.'