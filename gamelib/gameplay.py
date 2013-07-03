from minigame.dialogs.questions import ask_to_continue
import random

players = ['kyle', 'jill', 'kelly', 'jessica']
player = 'kyle'
pickedUpDice = 0
pickedUp = False
aRoll = []
pickedDice = []

def roll():
    global aRoll
    global pickedUpDice
    if pickedUpDice == 6:
        pickedUpDice = 0
    aRoll = [0]*(6-pickedUpDice)
    for i in range(len(aRoll)):
        aRoll[i] = random.randrange(1,7)
    print 'rolled',
    print ', '.join(map(str, aRoll))
    pick_up()

def ask_to_pickup(num):
    print 'would you like to pickup {}?\n(yes or no):'.format(num),
    return raw_input().lower().startswith('y')

def pick_up():
    global aRoll
    global pickedUpDice
    global pickedDice
    global pickedUp

    res = raw_input('will you pickup?(y or n):')
    if res.lower().startswith('y'):
        pickedUp = True
        picked = []
        for i in aRoll:
            if ask_to_pickup(i):
                picked.append(i)
                pickedUpDice += 1
        pickedDice.append(picked)
        #print 'set pickedUp to what num?',
        #pickedUpDice = int(raw_input())
    else:
        pickedUp = False

def change_player():
    global player
    global players
    global pickedDice
    global pickedUpDice

    pickedDice = []
    pickedUpDice = 0
    p = get_player()
    if p == (len(players) - 1):
        p = 0
    else:
        p += 1
    print 'changing player from  {0} to {1}'.format(player,players[p])
    player = players[p]

def get_player():
    global player
    global players
    return players.index(player)




def start_roll(name='kyle'):
    global pickedUpDice
    global pickedDice
    global pickedUp
    roll()
    if not pickedUp:
        change_player()
        start_roll()
    else:
        while pickedUp:
            if pickedUpDice != 6:
                print 'picked up {}'.format(', '.join(map(str, pickedDice)))
                if ask_to_continue('roll again'):
                    roll()
                else:
                    change_player()
                    start_roll()
            else:
                print 'gotta roll again'
                start_roll()
        else:
            change_player()
            start_roll()

def main():
    start_roll()

if __name__ == "__main__":
    main()
