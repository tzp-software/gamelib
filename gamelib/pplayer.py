import sys
class Player(object):
    _playerCount = 0
    _currentPlayerNum = 1
    #_players = PlayerMaker()
    _playerList = []

    @staticmethod
    def _get_current_player_name():
        for player in Player._playerList:
            if player.check_current_player():
                return player.get_name()

    @staticmethod
    def _get_current_player_num():
        return Player._currentPlayerNum

    #@staticmethod

    @staticmethod
    def _inc_player_count():
        Player._playerCount += 1
    inc_player_count = property(_inc_player_count)

    @staticmethod
    def _get_player_count():
        return Player._playerCount
    get_player_count = property(_get_player_count)


    def __init__(self, name):
        self.name = name
        Player._playerCount += 1
        self.set_num(Player._playerCount)
        self.score = 0
        Player._playerList.append(self)
        self.isCurrentPlayer = False
        self.heldDice = [][:]

    def __int__(self):
        return (6 - len(self.heldDice))

    def __str__(self):
        rtn = self.get_name()
        return rtn

    def __repr__(self):
        return self.name

    def __add__(self, other):
        ty = type(other)
        try:
            return str(self) + str(other)
        except TypeError('cannot add these'):
            sys.exit()
            

    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name

    def set_num(self, num):
        self.playerNum = num

    def get_num(self):
        return self.playerNum

    def check_current_player(self):
        return self.isCurrentPlayer        

    def change_current_player(self):
        if self.check_current_player():
            self.isCurrentPlayer = False
        else:
            self.isCurrentPlayer = True
        self.change_player()


    def change_player(self):
        current = Player._get_current_player_num()
        if current == Player._get_player_count():
            Player._currentPlayerNum = 1
        else:
            Player._currentPlayerNum += 1

    
    def add_score(self, score):
        self.score += int(score)


    def reset_held_dice(self):
        self.heldDice = [][:]

    
class PlayerMaker(object):
    def add_names(self, names):
        try:
            self.names.extend(names)
        except AttributeError:
            self.names = list(names)

    def make_players(self):
        '''return tuple of player objects
           generated from list of given names
        '''
        playerList = [0] * len(self.names)
        for name in range(len(self.names)):
            playerList[name] = Player(self.names[name])
        return playerList


c = PlayerMaker()
c.add_names(['kyle','jill','kelly'])
for i in c.make_players():
    print i.get_name()
