
'''
    __file__ = 'gamelib.dice.py'
    __author__ = 'Kyle Roux'
    __author_email__ = 'jstacoder@gmail.com'
    __date__ = 'Fri Jun 14 15:01:00 2013'
    __lisence__ = 'bsd'
'''
import random
import score

class RollRoller(object): 
    def __init__(self, roll):
       self.roll = roll

    def roll(self, num=1):
        for i in range(num):
            keepRolling = True
            dNum = 6
            while keepRolling:
                self.roll.roll()
                if not self.roll.get_score():
                   keepRolling = False 
                else:
                    res = raw_input('roll or stay?')
                    if res == 'roll'.lower():
                        keepRolling = True
                    else:
                        keepRolling = False

class DiceHolder(list):
    def append(self, item):
        super(DiceHolder, self).append(item)

    def __len__(self):
        count = 0
        for dice in self:
            count += len(dice)
        return count



class ARollDict(object): 
    def __init__(self, numberOfDice=6):
        '''initalize with a number of dice to roll
        or it will just default to 6. '''
        self.dieNum = numberOfDice
        self.num = 1

        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixs = 0

        self.dice = [0]*self.dieNum

    def add_one(self):
        self.ones += self.num

    def add_two(self):
        self.twos += self.num

    def add_three(self):
        self.threes += self.num

    def add_four(self):
        self.fours += self.num

    def add_five(self):
        self.fives += self.num

    def add_six(self):
        self.sixs += self.num

    def count_roll(self, roll):
        self.currentRoll = roll[:]
        for die in range(len(roll)):
            if int(roll[die]) == 1:
                self.add_one()
            elif int(roll[die]) == 2:
                self.add_two()
            elif int(roll[die]) == 3:
                self.add_three()
            elif int(roll[die]) == 4:
                self.add_four()
            elif int(roll[die]) == 5:
                self.add_five()
            elif int(roll[die]) == 6:
                self.add_six()
            else:
                raise ValueError, 'die value was {}'.format(roll)


    def reset_counts(self):
        for i in ['ones','twos','threes','fours','fives','sixs']:
            self.__dict__[i] = 0

    def get_counts(self):
        self.counts = {}.copy()
        for i in ['ones','twos','threes','fours','fives','sixs']:
            self.counts[i] = self.__dict__[i]
        self.reset_counts()
        return self.counts

    def __len__(self):
        return self.dieNum

    def __str__(self):
        return ' '.join(map(str,self.currentRoll))

    def __repr__(self):
        return str(self)

    def display_counts(self):
        rtn = 'you rolled {} dice and got:\n'.format(self.dieNum)
        count = self.get_counts()
        for x, y in count:
            rtn += 'you got {} {}\n'.format(x,y)
        self.reset_counts()
        return rtn

class CallableRoll(object):
    def __init__(self,num):
        self.dieNum = num
        self.roll()

    def roll(self,num=None):
        if num is not None:
            self.dieNum = num
        self.dice = get_dice(self.dieNum)

    def __call__(self, num=None):
        if num is not None:
            self.dieNum = num
        self.roll()
        return self.dice[:]

class RollException(Exception): 
    pass

class  Roll(CallableRoll):
    def __init__(self, dieNum=6):
        self.dieNum = dieNum
        self.rollCounter = ARollDict(self.dieNum)
        self.roll(self.dieNum)

    def __str__(self):
        return ' '.join(map(str, self.dice))

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.dice)

    def __getitem__(self, idx):
        if idx in self.currentRoll:
            return self.currentRoll[idx]
        #if idx < len(self.currentRoll):
        #    return self.currentRoll[idx]
        #else:
        #    raise IndexError
    def get_rolled_num(self):
        return self.dieNum

    def count_roll(self):
        self.rollCounter.count_roll(self.currentRoll)
        return self.rollCounter.get_counts()

    def set_current_roll(self):
        self.currentRoll = self.dice[:]

    def score_roll(self):
        scorer = score.Score(self.count_roll())
        return scorer.get_scores()

    def roll(self, num=None):
        self.rollCounter.counts = [][:]
        if num is not None:
            self.dieNum = num
        self.dice = get_dice(self.dieNum)
        self.set_current_roll()
        self.count_roll()
        #self.set_die_num()
        return self.currentRoll[:]

    def set_die_num(self):
        self.holder = DiceHolder()
        if self.score_roll() is not None:
            for dies in self.score_roll():
                self.holder.append(dies)
        else:
            self.dieNum = 6
            raise RollException('No dice Held')

        self.dieNum -= len(self.holder)
        if self.dieNum <= 0:
            self.dieNum = 6

def get_dice(num):
    dice = [0]*num
    for die in range(len(dice)):
        dice[die] = roll_die()
    return dice

def roll_die():
    return random.randrange(1,7)

def test2():
    kyle = {'Player1':'Kyle'}
    kyle['roll'] = CallableRoll(6)
    x1 = kyle['roll']()
    x2 = kyle['roll'](4)
    x3 = kyle['roll'](2)
    x4 = kyle['roll']()
    for i in [x1,x2,x3,x4]:
        print i 

def test():
    roll = ARollDict(6)
    dice = [0]*6
    for x in range(len(dice)):
        dice[x] = roll_die()
    roll.count_roll(dice)
    print roll
    #print roll.display_counts()

    newRoll = Roll(6)
    print newRoll
    newRoll.roll(4)
    print newRoll
    print newRoll.count_roll()
    #print newRoll.rollCounter.display_counts()
    print newRoll.roll(6)
    print newRoll
    print newRoll.count_roll()
    #print newRoll.rollCounter.display_counts()


def test3():
    roll = Roll(6)
    roll.roll()
    print roll
    print roll.score_roll()
    s = RollRoller(roll)
    s.roll()

def main():
    test()
    test2()
    test3()

if __name__ == "__main__":
    main()


