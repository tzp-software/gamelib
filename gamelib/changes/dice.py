'''
    dice.py
possible future version of dice.py
'''

import random

class Die(object):
    ''' represents a simple, single six sided die, unless you instantiate it otherwise'''
    _faces = (None,'One','Two','Three','Four','Five','Six')

    def __init__(self, diffNum=None):
        self.dieNum = 6
        if diffNum is not None:
            self.dieNum = diffNum

        if self.dieNum == 6:
            self.faces = Die._faces

        self.value = None
        self.values = range(1, self.dieNum+1)

    def __str__(self):
        if self.value is None:
            return 'Unrolled'
        else:
            return str(self.value)

    def __repr__(self):
        if self.value is None:
            return str(self)
        else:
            return self.faces[int(self.value)]

    def __contains__(self, item):
        return item in self.values

    def __len__(self):
        return self.dieNum

    def __add__(self, other):
        if type(self) == type(other):
            return (self, other)
        elif type(other) == type([]):
            other.append(self)
            return other
        else:
            raise ValueError('Cannot addd these')

    


