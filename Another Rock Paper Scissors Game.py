# Yet another game of Rock Paper Scissors

import os
import random
from time import sleep

options = {"R": "Rock", "P": "Paper", "S": "Scissors"}


def clear_screen():
    """Clear screen between games"""
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')


def play_game():
    """General function to call game play"""
    clear_screen()
    user_choice = input("Please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors\n>>> ").upper()
    if user_choice in list(options.keys()):
      print("You have selected {}.".format(options[user_choice]))
    else:
      print("Please select a valid option")
      exit()
    print("The computer is now selecting...")
    sleep(1)
    computer_choice = random.choice(list(options.keys()))
    print("The computer has selected {}.".format(options[computer_choice]))
    sleep(1)
    decide_winner(user_choice, computer_choice)


def decide_winner(user_choice, computer_choice):
    """Function call to decide winner of the game"""
    if user_choice == "P" and computer_choice == "R":
      print("You win")
    elif user_choice == "R" and computer_choice == "S":
      print("You win")
    elif user_choice == "S" and computer_choice == "P":
      print("You win")
    elif user_choice == computer_choice:
      print("You tied")
    else:
      print("You lost")


while __name__ == "__main__":
    play_game()
    quit_game = input("Continue? [Yn]\n>>> ").lower()
    if quit_game == 'n':
      break
