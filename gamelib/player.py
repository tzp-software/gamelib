'''
player.py
'''
import os
import random

debug = bool(os.getenv('DEBUG'))

class Player(object):
    _count = 0
    _current = 1
    _playerList = []

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.orderNum = 0
        self.isPlaying = False
        Player._count += 1
        Player._playerList.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @classmethod
    def _get_current_player_num(self):
        return Player._current

    def set_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def start_turn(self):
        self.isPlaying = True

    def end_turn(self):
        print Player._playerList[Player._current].get_name() + "'s turn is now over"
        self.isPlaying = False
        if self.orderNum == Player._count:
            self.change_player(1)
        else:
            self.change_player()

    def change_player(self, num=None):
        if num is not None:
            Player._current = num
        else: 
            if Player._current > Player._count or Player._current == 0:
                if debug:
                    print 'switching back to player 1'
                Player._current = 1
            else:
                if debug:
                    print 'switching to player {}'.format(Player._current+1)
                Player._current += 1
        Player._playerList[Player._current].start_turn()

    def check_playing(self):
        return self.isPlaying

    def set_order(self):
        random.shuffle(Player._playerList)
        #Player._playerList.insert(0,None)
        #for player in range(1,len(Player._playerList)):
        #    if Player._playerList[player] is not None:
        #        Player._playerList[player].orderNum = player+1

    def get_current(self):
        return self.check_current()

    def check_current(self):
        name = Player._playerList[Player._current].get_name()
        rtn = 'it\'s {}\'s turn'.format(name)
        return rtn
        

    def get_name(self):
        return self.name

class PlayerManager(object): 
    def __init__(self, players):
        self.players = players
        self.playerNum = len(players)



def main():
    x = Player('kyle')
    y = Player('jill')
    z = Player('jack')

    x.set_order()
    players = (x, y, z)
    turns = 9
    while turns != 0:
        for p in range(len(players)):
            print players[p].get_current()
            turns -= 1
            players[p].end_turn()
    '''
    print x.check_current()
    
    if x.check_playing():
        x.change_player()
    else:
        y.change_player()
    print x.check_current()

    if x.check_playing():
        x.change_player()
    else:
        y.change_player()
    print x.check_current()
    '''


if __name__ == "__main__":
    main()
