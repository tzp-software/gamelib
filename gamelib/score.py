'''
    gamelib.score.py
'''
#from dice import Roll as RollCounter
import dice

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
            return None




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
