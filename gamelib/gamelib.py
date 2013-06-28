'''
    __file__ = 'minigame.tools.util.py'
    __author__ = 'Kyle Roux'
    __author_email__ = 'jstacoder@gmail.com'
    __date__ = 'Wed May 29 13:02:39 2013'
    __lisence__ = 'bsd'
'''
import random
import sys
import os
import time

#sys.path.append('/Users/kyleroux/tzp/projects/minigame2')
from pplayer import Player, PlayerMaker
from rollmaker import RollMaker


ADD_PLAYER = 'Would you like to add another player?'

def check_debug():
    pass

def ask_bool(msg):
    ''' return bool True if response is y or yes and False if no or anything else '''
    msg = msg + '\n' + '(Yes or No): '
    return raw_input(msg).lower().startswith('y')


def ask_str(msg):
    ''' return with user input str after asking a str msg '''
    msg = msg + ': '
    return raw_input(msg)

def get_player_names():
    ''' return list of player names '''
    names = list()[:]
    addPlayer = True
    playerIncrement = 1
    while addPlayer:
        name = ask_str('Please enter a name for player# {}'.format(playerIncrement))
        names.append(name)
        playerIncrement += 1
        addPlayer = ask_bool(ADD_PLAYER)
    #else:
    #  print 'Playing: \n'
    #  print '\n'.join(map(str,names))
    return names

def get_random_first_player(lst, show=False):
    print 'Randomly assigning the order of play.',
    for i in range(5):
        time.sleep(2)
        print '.',
    if show:
        print '.' + '\n\n' + 'Order: '
    random.shuffle(lst)
    return lst

def get_player_order(lst, show=False):
    playerOrder = [][:]
    random.shuffle(lst)
    pnum = len(lst)
    if show:
        for player in lst:
            if player not in playerOrder:
                playerOrder.append(player)
                try:
                    player.set_num(playerOrder.index(player)+1)
                except Exception:
                    print player, type(player), lst 
                    print player.get_name() + ': player# ' + str(player.get_num())
    else:
        orderDict = {}
        for player in range(1,pnum+1):
            orderDict[str(player)] = lst[player-1]
        return orderDict


def get_die_roll(dieFaceNum=6):
    'returns an int between 1 and dieFaceNum'
    return random.randrange(1,dieFaceNum+1)

def get_dice_roll(dieFaceNum=6,dieNum=1):
    'return tuple of dieNum of dieFaceNum faced dice'
    lst = [0]*dieNum
    for i in range(len(lst)):
        lst[i] = get_die_roll(dieFaceNum)
    return tuple(lst)



def get_str(lstOrTuple):
    rtn = ''
    for i in lstOrTuple:
        rtn  +=  str(i) + ', '
    return rtn

def get_current_player(players):
    return players[players[0]._get_current_player_name()]

def get_current_player_name(order):
    return order[str(Player._get_current_player_num())]

def change_player(playerOrder):
    playerOrder['1'].change_current_player()

def ask_to_keep(order, dies):
    print dies
    player = get_current_player_name(order)
    if ask_bool('{} will you keep any dice?'.format(player)):
        dice = ask_str('Enter the faces, then hit enter: ')
        return str(dice).split(' ')
    else:
        change_player()


def roll(order, dNum=6):
    player = get_current_player_name(order)
    r = RollMaker(dNum)
    kept = ask_to_keep(player, r.roll(dNum))
    if kept is None:
        change_player(order)
        roll(order)
    else:
        ddnum = int(dNum)
        player.heldDice.extend(kept)    
        ddnum -= len(kept)
        if ddnum == 0:
            ddnum = 6
        if ask_bool('Will you keep the dice your holding and end your turn: '):
            player.reset_held_dice()
            change_player(order)
        else:
            roll(order, ddnum)


def test1():
    plist = get_player_names()
    playas = PlayerMaker()
    playas.add_names(plist)
    players = playas.make_players()
    p = get_random_first_player(players)
    order = get_player_order(p)
    for i in range(1,len(order)+1):
        print '\n\t{} is player {}'.format(order[str(i)],str(i))

    print roll(order, get_current_player_name(order))
    '''roller = RollMaker()
    print get_current_player_name(order) + ' rolled: \n'
    rtn = ''
    for i in ask_to_keep(get_current_player_name(order),str(roller.roll()).split(' ')):
        rtn += ', ' + i 

    print '{} is holding {}'.format(get_current_player_name(order),rtn)

    print roller.roll(4)
    change_player(order)

    print get_current_player_name(order) + 'rolled: \n'
    print roller.roll()
    print roller.roll(2)
    change_player(order)
    print get_current_player_name(order)
    change_player(order)
    print get_current_player_name(order)
    change_player(order)
    print get_current_player_name(order)
    '''
def test2():
    print get_dice_roll(6,6)

    x = get_dice_roll(6,6)
    print x
    def print_die_num(die,num):
        return die[:num]


    print print_die_num(x,2)
    print print_die_num(x,1)[0]

    print get_str(x) 
    


def test3():
    print 
    
def main():
    
    test1()
    test2()

if __name__ == "__main__":
    main()


