import sys

cont = input("Would you like to start the movie? Y/N ").lower()
if cont == 'n':
    sys.exit()
else:
    print("Enjoy the show!")