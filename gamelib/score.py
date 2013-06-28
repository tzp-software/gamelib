'''
    gamelib.score.py
'''
#from dice import Roll as RollCounter
from UserDict import UserDict
import dice

class RollCounter(dict): 
    _nums = ['ones','twos','threes','fours','fives','sixs']

    def __init__(self,roll=None):
        super(dict,self).__init__()
        self.reset_counts()
        try:
            if roll is not None:
                self.roll = roll[:]
                self.count_roll(roll)
        except ValueError:
            self.roll = roll[:]

    def reset_counts(self):
        for num in RollCounter._nums:
            self[num] = 0

    def count_roll(self, roll):
        self.roll = roll[:]
        self.reset_counts()
        for num in range(len(roll)):
            if int(roll[num]) == 1:
                self['ones'] += 1
            if int(roll[num]) == 2:
                self['twos'] += 1
            if int(roll[num]) == 3:
                self['threes'] += 1
            if int(roll[num]) == 4: 
                self['fours'] += 1
            if int(roll[num]) == 5:
                self['fives'] += 1
            if int(roll[num]) == 6:
                self['sixs'] += 1
            else:
                raise ValueError('need an int between 1 and 6, but i got {}'.format(roll[num]))


    def get_counts(self, roll=None):
        if roll is not None:
            self.count_roll(roll)
        return self





def make_roll(counts):
    roll = []
    try:
        for die in range(counts['ones']):
            roll.append(1)
    except KeyError:
        pass
    try:
        for die in range(counts['twos']):
            roll.append(2)
    except KeyError:
        pass
    try:
        for die in range(counts['threes']):
            roll.append(3)
    except KeyError:
        pass
    try:
        for die in range(counts['fours']):
            roll.append(4)
    except KeyError:
        pass
    try:
        for die in range(counts['fives']):
            roll.append(5)
    except KeyError:
        pass
    try:
        for die in range(counts['sixs']):
            roll.append(6)
    except KeyError:
        pass
    return roll


def test():
    counts = {'ones':0,'twos':0,'threes':5,'fours':0,'fives':1,'sixs':0}
    print make_roll(counts)
    x = Score(counts)
    print x.check_strait()
    print x.check_doubles()
    print x.n_of_a_kind()
    print x.get_leftovers()
    print x.get_scores()

class Score(object): 
    def __init__(self,rollCounts):
        self.new_roll(rollCounts)
        #self.dieNum = len(rollCounts.values())
        #self.used = []
        #self.roll = make_roll(rollCounts)
        #self.counts = rollCounts.copy()
        #self.set_scores()

    def new_roll(self, rollCounts):
        self.dieNum = len(rollCounts.values())
        self.used = []
        self.roll = make_roll(rollCounts)
        self.counts = rollCounts.copy()
        self.set_scores()

    def __len__(self):
        return len(self.scores)

    def check_strait(self):
        count = 0
        for i in self.counts:
            if self.counts[i] == 1:
                count += 1
        return count == 6

    def check_doubles(self):
        count = 0
        for i in self.counts.values():
            if i == 2:
                count += 1
        return count == 3

    def n_of_a_kind(self):
        minNum = 3
        rtn = []
        for i in self.counts:
            if self.counts[i] >= minNum:
                rtn.append(make_roll({i:self.counts[i]}))
        if len(rtn) < 1:
            return (None,)
        else:
            return tuple(rtn)


    def get_leftovers(self):
        leftover = []
        for i in ['ones','fives']:
            if self.counts[i] > 0 and self.counts[i] < 3:
                leftover.append(make_roll({i:self.counts[i]}))
        if len(leftover) > 0:
            return leftover
        else:
            return (None,)

    def set_scores(self):
        self.scores = [][:]
        for i in [self.check_strait(),self.check_doubles()]:
            if i:
                self.scores.append(self.roll)
                return tuple(self.scores)
        for i in self.n_of_a_kind():
            if i is not None:
                self.scores.append(i)
        for i in self.get_leftovers():
            if i is not None:
                self.scores.append(i)

    def get_scores(self):
        if len(self.scores) > 0:
            return tuple(self.scores)
        else:
            return tuple(None)




def test2():
    pass
    newRoll = dice.Roll(6)
    newRoll.roll()
    print newRoll
    score = Score(newRoll.count_roll())
    s = score.get_scores()
    if s is not None:
        print s
    else:
        print 'Your out! no Score!'


if __name__ == "__main__":
    test2()
