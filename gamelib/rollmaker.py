'''

    gamelib.rollmaker.py

'''
import random
import os
import sys
sys.path.append('/Users/kyleroux/tzp/projects/minigame2/minigame')



class RollMaker(object):
    def __init__(self, defaultNum=6):
        self.defaultNum = defaultNum

    def roll(self, num=None):
        if num is None:
            num = self.defaultNum
        return self.make_roll(int(num))

    def make_roll(self, num=None):
        if num is None:
            num = self.defaultNum
        return [random.randrange(1,7) for die in range(num)]


def main():
    import dieprinter as dp

    x = RollMaker()
    
    x.roll()

    print x.roll()
    print x.roll(3)

if __name__ == "__main__":
    main()
