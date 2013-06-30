'''
some dice rolling simulations
'''

import sys
import time
import random
from score import Score
from dice import Roll


def clear_screen():
    ' clear all text from the screen'
    x = '\n'*50
    print x
    time.sleep(1)


    
def player_say(text):
    ' put a convenient PLAYER label over text printed'
    print 'PLAYER:\n'
    print text
    print

def roll(num):
    'Roll object factory justs returns a Roll object' 
    return Roll(num)

def count_score(scoredRoll):
    'return an int of the number of numbers in SCORE'
    count = 0
    s = str(scoredRoll)
    for char in s:
        try:
            int(char)
            count += 1
        except ValueError:
            pass
    return count

def get_number_diff(num1, num2):
    ' give the difference of two numbers, they must be ints(or able to be ints)'
    if num1 >= num2:
        rtn = num1 - num2
    else:
        rtn = num2 - num1
    return rtn

def choose_to_stay(heldItems):
    ' give a tuple of lists and decied if the player will stay or not'
    if len(heldItems) >= 6:
        return True
    else:
        return False

def roll_dice(num=6, combos=None):
    ''' give an optional number of dice to roll(default 6)
        and a list of lists of numbers from rolled dice(also optional)
        and this will roll then until it either stays or quits, gathering 
        the held dice and returning them as it goes
    '''
    if not combos:
        heldCombos = []
    else:
        heldCombos = combos[:]
    print 'you are rolling {} dice'.format(num)
    aRoll = roll(num)
    time.sleep(2)
    print 'you rolled {}'.format(aRoll)
    score = aRoll.score_roll()
    held = count_score(score)
    time.sleep(2)
    if score is not None:
        print 'you held {}'.format(score)
        for combo in score:
            heldCombos.append(combo)
        d = get_number_diff(num, held)
        time.sleep(2)
        print 'You are now holding:\n{}'.format(heldCombos)
        time.sleep(2)
        print 'Now you have to decied to stay and keep your score......'
        print 'Or to risk it and roll again.....'
        time.sleep(2)
        if choose_to_stay(heldCombos):
            player_say('I will stay and keep \n{}'.format(heldCombos))
            print 'Turn Over'
            return False
        else:
            player_say('I will keep rolling')
            time.sleep(2)
    else:
        print 'you held nothing??? Turn over'
        return False

    if d == 0:
        d = 6
    time.sleep(2)
    print 'the next roll will be {} dice'.format(d)
    time.sleep(2)
    return (d, heldCombos)


def main():
    'make sure to split the arguments before sending them to roll_dice'
    clear_screen()
    x = roll_dice()
    while x:
        x = roll_dice(x[0],x[1])

    #rlist = [random.randrange(1,7) for x in range(10)]
    #for num in rlist:
    #    roll_dice(num)

if __name__ == "__main__":
    main()

