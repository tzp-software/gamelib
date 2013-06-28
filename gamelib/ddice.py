'''
ddice.py
'''
import random

class Die(object):
    _faces = (None,'One','Two','Three','Four','Five','Six')

    def __init__(self):
        self.faces = Die._faces[:]
        self.value = None

    def __str__(self):
        if not self.value:
            return 'Unrolled'
        else:
            return str(self.value)

    def __repr__(self):
        return str(self)

    def __int__(self):
        if self.value:
            return self.value
        else:
            raise ValueError('Unrolled die has no int value')

    def roll(self):
        self.value = random.randrange(1,7)
        return self.value

    def get_value(self):
        return self.value



class Roll(list):
    def __init__(self, dieNum=6):
        self.dieNum = dieNum
        for i in range(dieNum):
            self.append(Die())
            self[i].roll()

    def __str__(self):
        return ','.join(map(str,self))

    def __repr__(self):
        return str(self)

    def roll(self, num=None):
        if num is not None:
            dieNum = num

        self = Roll(self.dieNum)

    def get_roll(self):
        return self

