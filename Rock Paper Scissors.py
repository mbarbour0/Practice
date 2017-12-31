#  Let's play rps
from time import sleep
from random import randint

options = ['R', 'P', 'S']

lost = 'You lost!'
win = 'You won!'

def decide_winner(user_choice, computer_choice):
  print user_choice
  print 'Computer selecting...'
  sleep(1)
  print computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print 'You tied'
  elif user_choice_index == 0 and computer_choice_index == 2:
    print win
  elif user_choice_index == 1 and computer_choice_index == 0:
    print win
  elif user_choice_index == 2 and computer_choice_index == 1:
    print win
  else:
    print lost
  
def play_RPS():
  print 'You are now playing Rock, Paper, Scissors..'
  user_choice = raw_input('Please choose R for Rock, P for Paper, or S for Scissors')
  user_choice = user_choice.upper()
  if user_choice == options[0] or user_choice == options[1] or user_choice == options[2]:
    sleep(1)
    computer_choice = randint(0, len(options)- 1)
    computer_choice = options[computer_choice]
    decide_winner(user_choice, computer_choice)
  else:
    print 'You have entered an invalid selection, please try again'
play_RPS()