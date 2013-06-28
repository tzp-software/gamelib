import random

#######
#*       *# 
#     *    #
# *      *#
#######

VERT1 = '#######'
VERT2 = '####### #######'
VERT3 = '####### ####### #######'

MID1 = '#{}#'
MID2 = '#{}# #{}#'
MID3 = '#{}# #{}# #{}#'

ONE = {'top':'           ', 'mid':'     *    ', 'bot':'           '}
TWO = {'top':'          *', 'mid':'           ', 'bot':'*          '}
THREE = {'top':'          *', 'mid':'     *     ', 'bot':'*          '}
FOUR = {'top':'*        *', 'mid':'           ', 'bot':'*        *'}
FIVE = {'top':'*        *', 'mid':'     *     ', 'bot':'*        *'}
SIX = {'top':'*   *   *', 'mid':'           ', 'bot':'*   *   *'}

dies = [None, ONE, TWO,THREE,FOUR,FIVE, SIX]

def print_die(num):
    DIE = dies[num]
    rtn = '\n'
    rtn = VERT1 + rtn + MID1.format(DIE['top']) + rtn + MID1.format(DIE['mid']) + rtn + MID1.format(DIE['bot']) + rtn + VERT1
    return rtn



def print_dice(nums):
    if len(nums) == 1:
        n = nums[0]
        return print_die(n)
    elif len(nums) == 2:
        
        pass
    

def print_rand():
    print print_dice([random.randrange(1,7)])

def test():
    print_rand()

if __name__ == "__main__":
    test()
