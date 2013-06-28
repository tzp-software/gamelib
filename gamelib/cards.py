'''
    __name__ = 'gamelib.cards.py'
    
''' 
import random

ERR_SUIT = 'Need a suit'
ERR_RANK = 'Need a rank'

class Card(object):
    '''Represents a standard Playing card.
    h = hearts
    c = clubs
    d = diamonds
    s = spades
    
    A = ace = 1
    2-10 = 2-10
    J = jack = 11
    Q = queen = 12
    K = king = 13
    
    ie: Card(h,1) == aceOfHearts
    or  Card(d,7) == sevenOfDiamonds
    '''
    
    suits = dict(h='hearts',c='clubs',d='diamonds',s='spades')
    ranks = list((None,'a',2,3,4,5,6,7,8,9,10,'j','q','k'))    
    
    def __init__(self, suit=None, rank=None):
        if suit:
            self.suit = suit
        else:
            raise ValueError(ERR_SUIT)
        if rank:
            self.rank = rank
        else:
            raise ValueError(ERR_RANK)
        
    def __str__(self):
        return '{} of {}'.format(Card.ranks[self.rank], Card.suits[self.suit])


class Deck(object):
    '''an unshuffled deck of cards 52'''
    def __init__(self):
        self.cards = []
        for suit in suits.keys():
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
                
    def __str__(self):
        rtn = []
        for card in self.cards:
            rtn.append(str(card))
        return '\n'.join(rtn)
    
    def pop_card(self):
        self.cards.pop()
        
    def add_card(self, card):
        self.cards.append(card)
        
    def deal_hand(self, num):
        hand = Hand()
        for i in range(num):
            hand.add_card(Card(random.choice(suits.keys()),random.randrange(1,14)))
        return hand
        
        
class Hand(Deck):
    ''' represents a hand of cards
    initalize with Hand(type='poker',maxNum=7)
    '''
    def __init__(self,tpe=None,maxNum=10):
        self.cards = []
        self.label = tpe
        
def make_deck():
    return Deck()

def shuffle_deck(deck):
    random.shuffle(deck.cards)
    
suits = dict(h='hearts',c='clubs',d='diamonds',s='spades')
ranks = list((None,'ace',2,3,4,5,6,7,8,9,10,'jack','queen','king'))

def main():
    card = Card(random.choice(suits.keys()),random.randrange(1,14))
    print card

    deck = make_deck()
    print deck

    shuffle_deck(deck)
    print deck
    
    print 'Now a hand' 
    print
    print 
    
    hand = deck.deal_hand(7)
    print hand
    
    
    try:
        import dumshit as wack
    except ImportError:
        wack = None
    
    if wack:
        print 'doing wack things'
    else:
        print 'woo hoo you rock'
        
if __name__ == "__main__":
    main()