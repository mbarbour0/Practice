from random import randint

user_guess = raw_input('Enter R for Rock, P for Paper, or S for Scissors: ')
ug = user_guess.upper()
if ug not in ['R','P','S']:
    print 'Please pick a correct selection.'
    quit()

def comp():
    guess_index = randint(0,2)
    comp_guess = ['R','P','S'][guess_index]
    return comp_guess

def rpc():
    cg = comp()
    print 'The computer picks %s.' % (cg)
    if ug == cg:
        print 'You Tied'
    elif ug == 'R' and cg == 'S':
        print 'You Win!'
    elif ug == 'P' and cg == 'R':
        print 'You Win!'
    elif ug == 'S' and cg == 'P':
        print 'You Win!'
    else:
        print 'You Lose!'
        
rpc()