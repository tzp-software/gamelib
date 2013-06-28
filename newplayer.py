'''
    newplayer.py
'''
__author__ = 'Kyle roux'

import random

def make_player_list():
    pass

def set_random_order(playerList):
    random.shuffle(playerList)

class BasePlayer(object): 
    _playerCount = 0

    def __init__(self, name=None):
        BasePlayer._playerCount += 1
        self._playerNumber = BasePlayer._playerCount
        self._score = 0
        self._isPlaying = False
        if name is not None:
            self._name = name
        else:
            self._name = 'Player #{}'.format(self._playerNumber)

    def _get_name(self):
        return self._name

    def _get_score(self):
        return self._score

    def _set_score(self, score):
        assert score >= 1
        self._score += score

    def _update_is_playing(self):
        if self._isPlaying:
            self._isPlaying = False
        else:
            self._isPlaying = True

    def _get_is_playing(self):
        return self._isPlaying

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name



class PlayerManager(object): 
    def __init__(self):
        self.playerList = [][:]
        self.playerCount = 0
        self.playerScores = {}
        self.playerOrder = {}
        self.playerDict = {}

    def add_player(self, name):
        player = BasePlayer(name)
        self.playerCount += 1
        self.playerList.append(player)
        self.playerDict[player._name] = player
        self.playerScores[player._name] = self.playerDict[player._name]._get_score()

    def set_player_order(self):
        random.shuffle(self.playerList)
        for player in range(len(self.playerList)):
            num = int(player) + 1
            self.playerOrder[str(num)] = self.playerList[player]

    def set_score(self, player, score):
        assert isinstance(self.playerDict[player], BasePlayer)
        self.playerDict[player]._set_score(score)
        return 0

    def get_score(self, playerName=None):
        if playerName is not None:
            return self.playerDict[playerName]._get_score()
        else:
            rtn = ''
            for player in self.playerDict:
                rtn += 'NAME: ' + player + '  SCORE: ' + str(self.playerDict[player]._get_score()) + '\n'
            return rtn


    def get_first_player(self):
        return self.playerOrder[str(1)]

    def get_player_list(self):
        return self.playerList

    def __len__(self):
        return self.playerCount

def test():
    manager = PlayerManager()
    add = True
    while add:
        name = raw_input('Please enter a name for player {}: '.format(len(manager)+1))
        manager.add_player(name)
        add = raw_input('add another?\n(Y or N): ').lower().startswith('y')
    print 'added {} players'.format(len(manager))
    manager.set_player_order()
    print 'First player is {}'.format(manager.get_first_player())

if __name__ == "__main__":
    test()


