from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input('Enter your guess: '))
  return user_guess

def roll_dice():
  number_of_sides = int(raw_input('Enter the number of sides your dice has: '))
  if number_of_sides > 1:
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    total_roll = first_roll + second_roll
    max_val = number_of_sides * 2
    print 'The maximum roll you can achieve is %s' % (str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if user_guess <= max_val and user_guess >= 2:
      print 'Rolling...'
      sleep(2)
      print 'The computer\'s first roll is %d.' % (first_roll)
      sleep(1)
      print 'The computer\'s second roll is %d.' % (second_roll)
      sleep(1)
      print 'The computer\'s total roll is %d.' % (total_roll)
      sleep(1)
      if user_guess > total_roll:
        print 'Looks like you win this time.'
        return
      elif user_guess < total_roll:
        print 'You lose this one biosack.'
        return
      elif user_guess == total_roll:
        print 'Your human brain has guessed my number, somehow.'
        return
      
    else:
      print 'Enter a valid guess'
      return
  else:
    print 'Enter a valid number of sides for your dice.'
    return

roll_dice()