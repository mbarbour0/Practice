#dice game

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input('What\'s your guess? '))
  return guess

def roll_dice():
  sides = int(input('How many sides do your dice have? '))
  if sides >0:
    first_roll = randint(1, sides)
    second_roll = randint(1, sides)
    max_val = sides * 2
    print ("This is the highest possible roll " + str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if (user_guess > max_val) or user_guess == 1:
      print ('Your guess of ' + str(user_guess) + ' is invalid')
    else:
      print ('Rolling...')
      sleep(2)
      print ('The first roll is ' + str(first_roll))
      sleep(1)
      print ('The second roll is ' + str(second_roll))
      sleep(1)
      total_roll = first_roll + second_roll
      print (total_roll)
      print ('Result...')
      sleep(1)
      if user_guess > total_roll:
        print ('You did it, you won!!')
      elif user_guess < total_roll:
        print ('You lose, better luck next time..')
      elif user_guess == total_roll:
        print ('You tied, I demand a rematch!')
  else:
    print('You have attempted to cheat me!')

roll_dice()