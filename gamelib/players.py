'''
    gamelib.players.py
'''
__name__ = 'gamelib.players.py'
__author__ = 'Kyle Roux'
__author_email__ = 'jstacoder@gmail.com'
__version__ = '0.0.1'
__description__ = 'Definitions to aide in player use in games'
__url__ = 'http://github.com/tzpsoftware/'

# TODO BasePlayer
# TODO get_first


class BasePlayer(object): 
    'A player keeps track of name, number and score'
    _playerCount = 0
    def __init__(self, name):
        BasePlayer._playerCount += 1
        self.name = name
        self.score = 0
        self.playerNumber = BasePlayer._playerCount

    def __str__(self):
        rtn = 'Player# {}'.format(self.playerNumber)
        rtn += '\n' + self.name
        rtn += '\n' + 'SCORE: ' + str(self.get_score())
        return rtn

    def __repr__(self):
        return str(self)

    def __len__(self):
        return 1

    def set_score(self, score):
        self.score += score
        return self.score

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name


