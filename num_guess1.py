import random

def game():
    secret_num = random.randint(1,10)
    guesses = []
    attempt = 0
    
    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't even a number!".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}.".format(secret_num))
                break
            elif guess > secret_num:
                print("My number is lower than {}.".format(guess))
            elif guess < secret_num:
                print("My number is higher than {}.".format(guess))
            else:
                print("Miss. Enter a valid number between 1 and 10.")
            guesses.append(guess)
            print(guesses)
    else:
        print("You didn't get it, my number was {}.".format(secret_num))
    play_again = input("Do you want to play again? Y/N ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye")
game()