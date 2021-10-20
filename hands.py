import re
from operator import *
from constants import *

def sortCards(hand):
    """ Sort hand according to rank """
    sorted_hand = sorted(hand, key=itemgetter(2))
    return sorted_hand
   
def scoreHand(hand):
    ## Some preliminary necessities
    sorted_hand = sortCards(hand)
    rank_string = rankString(sorted_hand)

    ## Finding all possible hands 
    if findFlush(hand) != 0 and findStraight(sorted_hand) != 0 and sorted_hand[-1][2] == 14:
        score = 'royalflush'
    elif findFlush(hand) != 0 and findStraight(sorted_hand) != 0:
        score = 'strflush'
    elif fourKind(rank_string) != 0:
        score = 'fourkind'
    elif findFlush(hand) != 0:
        score = 'flush'
    elif threeKind(rank_string) != 0 and twoPair(rank_string) != 0:
        score = 'fullhouse'
    elif threeKind(rank_string) != 0:
        score = 'threekind'
    elif twoPair(rank_string) != 0:
        score = 'twopair'
    elif findPair(rank_string) != 0:
        score = 'onepair'
    elif findStraight(sorted_hand) != 0:
        score = 'straight'
    else:
        score = 'highcard'

    return score


def rankString(hand):
    """ Creates a string so that RE can be used to find pairs, three and four of a kind. """
    rankhand = []
    for card in hand:
        rankhand.append(card[0])
    rank_string = ''.join(rankhand)
    return rank_string

def findPair(string):
    """ Find a pair """
    pair = re.compile(r".*(.).*\1")
    try:
        m = pair.match(string).groups()
    except:
        return 0

def twoPair(string):
    """ Find two pairs """
    twopair = re.compile(r".*(.).*\1.*(.).*\2")
    try:
        m = twopair.match(string).groups()
    except:
        return 0

def threeKind(string):
    """ Find three of a kind """
    threeof = re.compile(r".*(.).*\1.*\1")
    try:
        m = threeof.match(string).groups()
    except:
        return 0

def fourKind(string):
    """ Find four of a kind """
    fourof = re.compile(r".*(.).*\1.*\1.*\1")
    try:
        m = fourof.match(string).groups()
    except:
        return 0

def findStraight(hand):
    """ Find a straight """
    if hand[4][2] == (hand[3][2] + 1) and hand[3][2] == (hand[2][2] + 1) and hand[2][2] == (hand[1][2] + 1) and hand[1][2] == (hand[0][2] + 1):
        return 1
    else:
        return 0

def findFlush(hand):
    """ Find a flush """
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return 1
    else:
        return 0
